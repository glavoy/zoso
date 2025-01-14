from django.urls import path
from .views import *
from . import api


# All of the URL's for the projewct
urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/contacts/add', AddContact.as_view(), name='add-contact'),
    path('profile/<int:pk>/contacts/remove', RemoveContact.as_view(), name='remove-contact'),
    path('search/', SearchUserView.as_view(), name='user-search'),
    path('contacts/<int:pk>/', ContactsView.as_view(), name='contacts'),
    path('chat/<int:pk>/', SelectChatView.as_view(), name='selectchat'),
    path('chat/<str:roomname>/', ChatRoomView.as_view(), name='chatroom'),


    # API URL's
    path('api/', api.zoso_api_root, name='zoso_api_root'),
    path('api/users', api.UserList.as_view(), name='users_api'),
    path('api/user/<int:pk>/', api.UserDetail.as_view(), name='user_api'),
    path('api/profiles', api.ProfileList.as_view(), name='profiles_api'),
    path('api/profile/<int:pk>/', api.ProfileDetail.as_view(), name='profile_api'),       
    path('api/posts', api.PostList.as_view(), name='posts_api'),
    path('api/post/<int:pk>/', api.PostDetail.as_view(), name='post_api'),
    path('api/comments', api.CommentList.as_view(), name='comments_api'),
    path('api/comment/<int:pk>/', api.CommmentDetail.as_view(), name='comment_api'),
    path('api/chats', api.ChatList.as_view(), name='chats_api'),
    path('api/chat/<int:pk>/', api.ChatDetail.as_view(), name='chat_api'),
    path('api/chatrooms', api.ChatRoomList.as_view(), name='chatrooms_api'),
    path('api/chatroom/<int:pk>/', api.ChatRoomDetail.as_view(), name='chatroom_api'),
 
]
