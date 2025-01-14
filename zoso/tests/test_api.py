# The code below tests all the api's in the application
import json
from unittest.case import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from ..serializers import *
from django.test import  Client
from rest_framework import status
import datetime
from django.utils.timezone import make_aware

# initialize the APIClient app
client = Client()


# Test API for viewing a user
class UserDetailTest(APITestCase):
    user = None
    good_url = ''
    bad_url = ''

    # Set up some data to test
    def setUp(self):
        self.user = User.objects.create_user(username='jpafghge', email='jpfghage@zep.com', first_name='Jimmy', last_name='Page', password='zosozoso')
        # Valid URL
        self.good_url = reverse('user_api', args=[1])
        # Invalid URL
        self.bad_url = "api/user/999"

    def tearDown(self):
        User.objects.all().delete()

    # Test status code successful with URL that contains valid data
    def test_returns_code_200_with_valid_url(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)

    # Test status code not successful with URL that contains ionvalid data
    def test_returns_code_404_with_invalid_url(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)



# Test API for creating a new user
# Tests both valid data and invalid data (missing username)
class CreateNewUser(TestCase):
    valid_data = None
    invalid_data = None

    def setUp(self):
        self.valid_data = {
                            'username': 'mynewusername',
                            'email': 'aaa@bbb.com',
                            'first_name': 'First Name',
                            'last_name': 'Last Name',
                            'password': 'xxxxxxx'
                        }
        self.invalid_data = {
                            'username': '',
                            'email': '',
                            'first_name': 'First Name',
                            'last_name': 'Last Name',
                            'password': 'xxxxxxx'
                        }

    # Test Posting a new user with valid data
    def test_create_valid_data(self):
        response = client.post(
            reverse('user_api', args=[1]),
            data=json.dumps(self.valid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test Posting a new user with invalid data (missing username)
    def test_create_invalid_data(self):
        response = client.post(
            reverse('user_api', args=[1]),
            data=json.dumps(self.invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)







# # Test API for viewing a profile
class ProfileDetailTest(APITestCase):
    profile = None
    good_url = ''
    bad_url = ''

    # Set up some data to test
    def setUp(self):
        self.profile = Profile.objects.create(fullname="Jimmy Page", about="Guitarist Extraordinaire", location="London")
        # Valid URL using the post created above
        self.good_url = reverse('profile_api', kwargs={'pk': 1})
        # Invalid URL since the id does not exist
        self.bad_url = "api/profile/9987"

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    # Test status code successful with URL that contains valid data
    def test_returns_code_200_with_valid_url(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)

    # Test status code not successful with URL that contains ionvalid data
    def test_returns_code_404_with_invalid_url(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)





# Test API for creating a profile
class CreateNewProfile(TestCase):
    user = None
    valid_data = None
    invalid_data = None
    test_user1  = None
    def setUp(self):
        self.test_user1  = User.objects.create_user(username='yrttyytytytytytyty', email='jacgggob@ddd.com', password='top_secret')
        self.test_user1.save()
        self.valid_data = {
                            'user': self.test_user1.id,
                            'fullname': 'retert',
                            'about': 'ertte',
                            'location': 'ertet',
                        }
        self.invalid_data = {
                            'user': 44,
                            'fullname': 'retert',
                            'about': 'ertte',
                            'location': 'ertet',
                        }

    # Test Posting with invalid data
    def test_create_invalid_data(self):
        response = client.post(
            reverse('profile_api', args=[23]),
            data=json.dumps(self.invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)





# Test API for viewing a Post
class PostDetailTest(APITestCase):

    post = None
    good_url = ''
    bad_url = ''

    # Set up some data to test
    def setUp(self):
        # Set up a Post object for the test methodsf
        self.user = User.objects.create(username='jafghfgcob', email='jafghcob@ddd.com', password='top_secret')
        self.post = Post.objects.create(text="Very cool pic!", createdon=make_aware(datetime.datetime.now()), createdby=self.user)
        # Valid URL using the post created above
        self.good_url = reverse('post_api', kwargs={'pk': 1})
        # Invalid URL since the id does not exist
        self.bad_url = "api/post/222"


    def tearDown(self):
        Post.objects.all().delete()
        User.objects.all().delete()


    # Test status code successful with URL that contains 
    # a protein_id in the database
    def test_returns_code_200_with_valid_url(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)

    # Test status code not successful with URL that contains 
    # a protein_id that is not in the database
    def test_returns_code_404_with_invalid_url(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)



# Test API for creating a new post
class CreateNewPost(TestCase):
    user = None
    valid_data = None
    invalid_data = None

    def setUp(self):
        self.invalid_data = {
                            'text': 'My new post',
                            'createdby': ""
                        }

    # Test Posting with invalid data
    def test_create_invalid_data(self):
        response = client.post(
            reverse('post_api', args=[1]),
            data=json.dumps(self.invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)





# Test API for viewing a Comment
class CommentDetailTest(APITestCase):

    comment = None
    good_url = ''
    bad_url = ''

    # Set up some data to test
    def setUp(self):
        self.user = User.objects.create_user(username='jpage', email='jpage@zep.com', first_name='Jimmy', last_name='Page', password='zosozoso')
        self.post = Post.objects.create(text="My fake post message", createdon=make_aware(datetime.datetime.now()), createdby=self.user)
        self.comment = Comment.objects.create(comment="My fake comment", createdon=make_aware(datetime.datetime.now()), createdby=self.user, post=self.post)

        # Valid URL using the post created above
        self.good_url = reverse('comment_api', kwargs={'pk': 1})
        # Invalid URL since the id does not exist
        self.bad_url = "api/comment/222"


    def tearDown(self):
        Comment.objects.all().delete()
        Post.objects.all().delete()
        User.objects.all().delete()


    # Test status code successful with URL that contains 
    # a protein_id in the database
    def test_returns_code_200_with_valid_url(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)

    # Test status code not successful with URL that contains 
    # a protein_id that is not in the database
    def test_returns_code_404_with_invalid_url(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)




# Test API for creating a new comment
class CreateNewComment(TestCase):
    invalid_data = None

    def setUp(self):
        self.invalid_data = {
                            'post': '',
                            'comment': 'My comment',
                        }

    # Test Posting invalid data
    def test_create_invalid_data(self):
        response = client.post(
            reverse('comment_api', args=[1]),
            data=json.dumps(self.invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



# Test API for viewing a Chatroom
class ChatRoomDetailTest(APITestCase):

    chatroom = None
    good_url = ''
    bad_url = ''

    # Set up some data to test
    def setUp(self):
        self.chatroom = ChatRoom.objects.create(roomname="goodroom")

        # Valid URL using the post created above
        self.good_url = reverse('chatroom_api', kwargs={'pk': 1})
        # Invalid URL since the id does not exist
        self.bad_url = "api/chatroom/222"


    def tearDown(self):
        ChatRoom.objects.all().delete()


    # Test status code successful with valid URL
    def test_returns_code_200_with_valid_url(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)

    # est status code successful with invalid URL
    def test_returns_code_404_with_invalid_url(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)



# Test API for creating a new chatroom
class CreateNewChatRoom(TestCase):
    valid_date = None
    invalid_data = None

    def setUp(self):
        self.valid_data = {
                            'roomname': 'myroom',
                        }
        self.invalid_data = {
                            'roomname': None,
                        }

    # Test Posting a new chatroom with valid data
    def test_create_valid_data(self):
        response = client.post(
            reverse('chatroom_api', args=[1]),
            data=json.dumps(self.valid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test Posting a new chatroom with invalid data 
    def test_create_invalid_data(self):
        response = client.post(
            reverse('chatroom_api', args=[1]),
            data=json.dumps(self.invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)




# Test API for viewing a Chat
class ChatDetailTest(APITestCase):
    user = None
    chatroom = None
    chat = None
    good_url = ''
    bad_url = ''

    # Set up some data to test
    def setUp(self):
        self.user = User.objects.create_user(username='jpage', email='jpage@zep.com', password='zosozoso')
        self.chatroom = ChatRoom.objects.create(roomname="goodroom")
        self.chat = Chat.objects.create(chattext="Hey, what's up?", timestamp=make_aware(datetime.datetime.now()), user=self.user, roomname=self.chatroom)

        # Valid URL using the post created above
        self.good_url = reverse('chat_api', kwargs={'pk': 1})
        # Invalid URL since the id does not exist
        self.bad_url = "api/chat/222"


    def tearDown(self):
        ChatRoom.objects.all().delete()


    # Test status code successful with valid URL
    def test_returns_code_200_with_valid_url(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)

    # est status code successful with invalid URL
    def test_returns_code_404_with_invalid_url(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)



# Test API for creating a new chat
class CreateNewChat(APITestCase):
    user = None
    chatroom = None
    chat = None    
    invalid_data = None


    def setUp(self):
        self.user = User.objects.create_user(username='jpage', email='jpage@zep.com', password='zosozoso')
        self.chatroom = ChatRoom.objects.create(roomname="goodroom")

        self.invalid_data = {
                            'user': self.user.id,
                            'chatroom': None,
                            'chattext': 'dfggdgdfg'
                        }


    # Test Posting a new user with invalid data (missing username)
    def test_create_invalid_data(self):
        response = client.post(
            reverse('comment_api', args=[self.chatroom.id]),
            data=json.dumps(self.invalid_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

