from django.shortcuts import render, redirect
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from .models import Post, Comment, Profile, Chat, ChatRoom
from django.views.generic.edit import UpdateView
from .forms import ChatForm, PostForm, CommentForm


# This view is used for the main page of the app.
# It uses a form to allow the user to add a post.
# It also gets all of the posts from the current user and 
# posts from all of their contacts as well.
# It uses the PostForm to allow user to add a post.
class PostListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        # Get a list of all the current users contacts
        contacts = list(Profile.objects.values_list('contacts', flat=True).filter(user=user.id))
        # Filter the posts by contacts as well as the current user
        posts = Post.objects.filter(Q(createdby__in=contacts) | Q(createdby=user.id)).order_by('-createdon')
        form = PostForm()

        context = {
            'post_list': posts,
            'form': form,
            'logged_in_user': user
        }

        return render(request, 'zoso/posts.html', context)

    def post(self, request, *args, **kwargs):
        user = request.user
        contacts = list(Profile.objects.values_list('contacts', flat=True).filter(user=user.id))
        posts = Post.objects.filter(Q(createdby__in=contacts) | Q(createdby=user.id)).order_by('-createdon')
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.createdby = request.user
            new_post.save()

        context = {
            'post_list': posts,
            'form': form,
        }

        return render(request, 'zoso/posts.html', context)



# This view is used to get and edit post details.
# Only the current user can edit their own posts
class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-createdon')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'zoso/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.createdby = request.user
            new_comment.post = post
            new_comment.save()

        comments = Comment.objects.filter(post=post).order_by('-createdon')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'zoso/post_detail.html', context)



# This View is used to edit a post. Only the author of the post can make an edit.
# It requires the use of the 'test_func', which verifies 
# that the user is the one who made the post.
class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['text']
    template_name = 'zoso/post_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.createdby



# This view is used to get a user profile
class ProfileView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        viewing_user = profile.user
        user = request.user
        posts = Post.objects.filter(createdby=viewing_user).order_by('-createdon')
        contacts = user.profile.contacts.all()

        if len(contacts) == 0:
            is_contact = False

        # Determine if the profile we are viewing is a contact of the current user
        for contact in contacts:
            if contact == profile.user:
                is_contact = True
                break
            else:
                is_contact = False

        # user: current user
        # profile: profile object of user to show
        # posts: post object of all posts of the user we want to view
        # is_contact: is_contact,
        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'is_contact': is_contact
        }

        return render(request, 'zoso/profile.html', context)



# This view is used to edit the users profile
class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields = ['profilepic', 'fullname', 'about', 'location']
    template_name = 'zoso/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user



# This View is used to add a contact for the user
class AddContact(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=request.user.id)
        # Add contact
        profile.contacts.add(pk)

        return redirect('profile', pk=pk)



# This View is used to remove a contact for the user
class RemoveContact(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=request.user.id)
        # Remove contact
        profile.contacts.remove(pk)

        return redirect('profile', pk=pk)



# This View is used to get the results of a search for a user
class SearchUserView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # This is the search query
        query = self.request.GET.get('query')
        # Find all matching profiles that contain the query, but exclude the user 'root'
        profile_list = Profile.objects.filter(Q(user__username__icontains=query) & ~Q(user__username='root'))

        return render(request, 'zoso/searchuser.html', {'profile_list': profile_list})



# This View is used to get the contacts of a user
class ContactsView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        contacts = profile.contacts.all()

        return render(request, 'zoso/contacts.html', {'contacts': contacts})



# This view is used to get a list of users to chat with.
# It uses the ChatForm to show contacts of current user
class SelectChatView(LoginRequiredMixin, View):

    # This passes the request object to the form class.
    # This is necessary because we want only the contacts
    # from the current user
    def get_form_kwargs(self):
        kwargs = super(SelectChatView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        contacts = profile.contacts.all()
        form = ChatForm(user=request.user)

        context = {
            'profile': profile,
            'contacts': contacts,
            'form': form,
        }

        return render(request, 'zoso/selectchat.html', context)

    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        contacts = profile.contacts.all()
        form = ChatForm(request.POST, user=request.user)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.createdby = request.user
            new_post.save()

        context = {
            'contacts': contacts,
            'form': form,
        }

        return render(request, 'zoso/chatroom.html', context)



# This view is used to get previous chats to be displayed
# in case the users chatting have a chat history. The chat
# history can then be displayed.
class ChatRoomView(LoginRequiredMixin, View):
    def get(self, request, roomname):
        chatroom = ChatRoom.objects.filter(roomname=roomname).first()

        timestamp = "timestamp"
        
        # Store the chats history here
        chats = []

        # If the chatroom already exists, get the previous chats
        if chatroom:
            chats = Chat.objects.filter(roomname=chatroom).order_by('-timestamp')
        # Otherwise create the chatroom
        else:
            chatroom = ChatRoom(roomname=roomname)
            chatroom.save()

        context = {
            'roomname': roomname,
            'chats': chats
        }

        return render(request, 'zoso/chatroom.html', context)
