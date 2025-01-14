from tkinter import Image
from django.test import TestCase
from ..models import *
import datetime
from django.utils.timezone import make_aware



# This class tests the Builtin User Model
class UserModelTest(TestCase):
    # Create an instance of the User model
    def setUp(self):
        # Create a user for the test methods
        self.user = User.objects.create_user(username='jpage', email='jpage@zep.com', password='zosozoso')

    # Test if 'username' field exists and is correct type
    def test_username_field_present(self):                   
        self.assertIsInstance(self.user.username, str)

    # Test if 'email' field exists and is correct type
    def test_email_field_present(self):                   
        self.assertIsInstance(self.user.email, str)
    
    # Test if 'password' field exists and is correct type
    def test_password_field_present(self):                   
        self.assertIsInstance(self.user.password, str)    

    # Clean up
    def tearDown(self):
        User.objects.all().delete()




# This class tests the Profile Model
class ProfileModelTest(TestCase):
    # Create an instance of the Profile model
    def setUp(self):
        # Set up a Profile object for the test methods
        self.user = User.objects.create_user(username='jpage', email='jpage@zep.com', password='zosozoso')
        self.profile = Profile.objects.create(fullname="Jimmy Page", about="Guitarist Extraordinaire", location="London")

    # Test that the string representation of the Profile model is correct
    def test_model_str(self):
        self.assertEqual(str(self.profile.fullname), "Jimmy Page")

    # Test if 'about' field exists and is correct type
    def test_about_field_present(self):                   
        self.assertIsInstance(self.profile.about, str)

    # Test if 'location' field exists and is correct type
    def test_location_field_present(self):                   
        self.assertIsInstance(self.profile.location, str)

    # Clean up
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        



# This class tests the Post Model
class PostModelTest(TestCase):
    # Create an instance of the Post model
    def setUp(self):
        # Set up a Post object for the test methods
        self.user = User.objects.create_user(username='jpage', email='jpage@zep.com', password='zosozoso')
        self.post = Post.objects.create(text="My fake post message", createdon=make_aware(datetime.datetime.now()), createdby=self.user)

    # Test that the string representation of the Post model is correct
    def test_model_str(self):
        self.assertEqual(str(self.post.text), "My fake post message")

    # Test if 'createdon' field exists and is correct type
    def test_createdon_field_present(self):                   
        self.assertIsInstance(self.post.createdon, datetime.datetime)

    # Test if 'createdby' field exists and is correct type
    def test_createdby_field_present(self):                   
        self.assertIsInstance(self.post.createdby, User)

    # Clean up
    def tearDown(self):
        Post.objects.all().delete()
        User.objects.all().delete()




# This class tests the Comment Model
class CommentModelTest(TestCase):
    # Create an instance of the Comment model
    def setUp(self):
        # Set up a Comment object for the test methods
        self.user = User.objects.create_user(username='jpage', email='jpage@zep.com', password='zosozoso')
        self.post = Post.objects.create(text="My fake post message", createdon=make_aware(datetime.datetime.now()), createdby=self.user)
        self.comment = Comment.objects.create(comment="My fake comment", createdon=make_aware(datetime.datetime.now()), createdby=self.user, post=self.post)

    # Test that the string representation of the Comment model is correct
    def test_model_str(self):
        self.assertEqual(str(self.comment.comment), "My fake comment")

    # Test if 'createdon' field exists and is correct type
    def test_about_field_present(self):                   
        self.assertIsInstance(self.comment.createdon, datetime.datetime)

    # Test if 'createdby' field exists and is correct type (User)
    def test_location_field_present(self):                   
        self.assertIsInstance(self.comment.createdby, User)

    # Test if 'post' field exists and is correct type
    def test_location_field_present(self):                   
        self.assertIsInstance(self.comment.post, Post)        

    # Clean up
    def tearDown(self):
        Comment.objects.all().delete()
        Post.objects.all().delete()
        User.objects.all().delete()




# This class tests the ChatRoom Model
class ChatRoomTest(TestCase):
    def setUp(self):
        self.chatroom = ChatRoom.objects.create(roomname="goodroom")

    # Test that the string representation of the ChatRoom model is correct
    def test_model_str(self):
        self.assertEqual(str(self.chatroom.roomname), "goodroom")
     
     # Test if 'roomanme' field exists and is correct type
    def test_roomname_field_present(self):
        self.assertIsInstance(self.chatroom.roomname, str)

    # Clean up
    def tearDown(self):
        ChatRoom.objects.all().delete()




# This class tests the Chat Model
class ChatModelTest(TestCase):
    # Create an instance of the Chat model
    def setUp(self):
        # Set up a Chat object for the test methods
        self.user = User.objects.create_user(username='jpage', email='jpage@zep.com', password='zosozoso')
        self.chatroom = ChatRoom.objects.create(roomname="goodroom")
        self.chat = Chat.objects.create(chattext="Hey, what's up?", timestamp=make_aware(datetime.datetime.now()), user=self.user, roomname=self.chatroom)

    # Test that the string representation of the Chat model is correct
    def test_model_str(self):
        self.assertEqual(str(self.chat.chattext), "Hey, what's up?")

    # Test if 'timestamp' field exists and is correct type
    def test_timestamp_field_present(self):                   
        self.assertIsInstance(self.chat.timestamp, datetime.datetime)

    # Test if 'user' field exists and is correct type
    def test_user_field_present(self):                   
        self.assertIsInstance(self.chat.user, User)

    # Test if 'roomname' field exists and is correct type
    def test_roomname_field_present(self):                   
        self.assertIsInstance(self.chat.roomname, ChatRoom)

    # Clean up
    def tearDown(self):
        Chat.objects.all().delete()
        ChatRoom.objects.all().delete()
        User.objects.all().delete()

