
from .models import *
from .serializers import *
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins


# This is the 'root' of the API
# It provides a link to each of the endpoints for easy navigation.
@api_view(['GET'])
def zoso_api_root(request, format=None):
    return Response({
        # Link to List all Users
        '1': reverse('users_api', request=request, format=format),
        # Link to View User details
        '2': reverse('user_api', request=request, format=format,args=[1]),
        # Link to view all User Profiles
        '3': reverse('profiles_api', request=request, format=format),
        # Link to view User Profile details
        '4': reverse('profile_api', request=request, format=format, args=[1]),                         
        # Link to view all Posts
        '5': reverse('posts_api', request=request, format=format),
        # Link to view Post details
        '6': reverse('post_api', request=request, format=format, args=[1]),
        # Link to view all Comments
        '7': reverse('comments_api', request=request, format=format),
        # Link to view Comment details
        '8': reverse('comment_api', request=request, format=format, args=[1]),
        # Link to view all Chats
        '9': reverse('chats_api', request=request, format=format),
        # Link to view Chat details
        '10': reverse('chat_api', request=request, format=format, args=[1]),
        # Link to view all Chatrooms
        '11': reverse('chatrooms_api', request=request, format=format),
        # Link to view Chatroom details
        '12': reverse('chatroom_api', request=request, format=format, args=[1]),                     
    })


# Class to view the list of users
# http://127.0.0.1:8000/zoso/api/users
class UserList(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer



# Class to view the details of a user
# http://127.0.0.1:8000/zoso/api/user/[id]
class UserDetail(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView ):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Class to view the list of profiles
# http://127.0.0.1:8000/zoso/api/profiles
class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# Class to view the details of a profile
# http://127.0.0.1:8000/zoso/api/profile/[id]
class ProfileDetail(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView ):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Class to view the list of posts
# http://127.0.0.1:8000/zoso/api/posts
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Class to view the details of a post
# http://127.0.0.1:8000/zoso/api/post/[id]
class PostDetail(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView ):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Class to view the list of comments
# http://127.0.0.1:8000/zoso/api/comments
class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# Class to view the details of a post
# http://127.0.0.1:8000/zoso/api/comment/[id]
class CommmentDetail(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView ):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Class to view the list of chats
# http://127.0.0.1:8000/zoso/api/chats
class ChatList(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


# Class to view the details of a chat
# http://127.0.0.1:8000/zoso/api/chat/[id]
class ChatDetail(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView ):

    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Class to view the list of chatrooms
# http://127.0.0.1:8000/zoso/api/chatrooms
class ChatRoomList(generics.ListAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


# Class to view the details of a chatroom
# http://127.0.0.1:8000/zoso/api/chatroom/[id]
class ChatRoomDetail(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView ):

    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)