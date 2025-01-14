# The code below tests all the serializers in the application

# Import modules
from django.test import TestCase
from ..serializers import *
import datetime
from django.utils.timezone import make_aware



# This class tests the User Serializer
class UserSerializerTests(TestCase):
    user = None
    userSerializer = None

    # Create instance of User model
    def setUp(self):
        self.user = User.objects.create_user(username='jpage', email='jpage@zep.com', first_name='Jimmy', last_name='Page', password='zosozoso')
        self.userSerializer = UserSerializer(instance=self.user)

    # Test to ensure all fields are present in the serializer
    def test_user_serializer_has_correct_fields(self):
        data = self.userSerializer.data
        self.assertEqual(set(data.keys()), set(['id', 'username', 'email', 'first_name', 'last_name', 'password']))

    # Test to ensure the id field is correct
    def test_user_serializer_has_correct_id(self):
        data = self.userSerializer.data
        self.assertEqual(data['id'], 1)

    # Test to ensure the username field is correct
    def test_user_serializer_has_correct_username(self):
        data = self.userSerializer.data
        self.assertEqual(data['username'], "jpage")
 
    # Test to ensure the email field is correct
    def test_user_serializer_has_correct_email(self):
        data = self.userSerializer.data
        self.assertEqual(data['email'], "jpage@zep.com")

    # Test to ensure the first_name field is correct
    def test_user_serializer_has_correct_first_name(self):
        data = self.userSerializer.data
        self.assertEqual(data['first_name'], "Jimmy")

    # Test to ensure the password field is correct
    def test_user_serializer_has_correct_last_name(self):
        data = self.userSerializer.data
        self.assertEqual(data['last_name'], "Page")    

    # Clean up
    def tearDown(self):
        User.objects.all().delete()




# This class tests the Profile Serializer
class ProfileSerializerTests(TestCase):
    user = None
    profile = None
    profileSerializer = None

    # Create instance of Profile model
    def setUp(self):
        self.user = User.objects.create_user(username='jpage', email='jpage@zep.com', first_name='Jimmy', last_name='Page', password='zosozoso')
        self.profile = Profile.objects.create(fullname="Jimmy Page", about="Guitarist Extraordinaire", location="London")
        self.profileSerializer = ProfileSerializer(instance=self.profile)

    # Test to ensure all fields are present in the serializer
    def test_profile_serializer_has_correct_fields(self):
        data = self.profileSerializer.data
        self.assertEqual(set(data.keys()), set(['user', 'fullname', 'about','location', 'profilepic', 'contacts']))

    # Test to ensure the fullname field is correct
    def test_profile_serializer_has_correct_fullname(self):
        data = self.profileSerializer.data
        self.assertEqual(data['fullname'], "Jimmy Page")
 
    # Test to ensure the about field is correct
    def test_profile_serializer_has_correct_about(self):
        data = self.profileSerializer.data
        self.assertEqual(data['about'], "Guitarist Extraordinaire")

    # Test to ensure the location field is correct
    def test_profile_serializer_has_correct_firstlocation(self):
        data = self.profileSerializer.data
        self.assertEqual(data['location'], "London")

    # Clean up
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()





# This class tests the Post Serializer
class PostSerializerTests(TestCase):
    user = None
    post = None
    postSerializer = None

    # Create instance of Post model
    def setUp(self):
        self.user = User.objects.create_user(username='jpage', email='jpage@zep.com', first_name='Jimmy', last_name='Page', password='zosozoso')
        self.post = Post.objects.create(text="My fake post message", createdby=self.user)
        self.postSerializer = PostSerializer(instance=self.post)

    # Test to ensure all fields are present in the serializer
    def test_post_serializer_has_correct_fields(self):
        data = self.postSerializer.data
        self.assertEqual(set(data.keys()), set(['id', 'text', 'image', 'createdon', 'createdby']))

    # Test to ensure the id field is correct
    def test_post_serializer_has_correct_id(self):
        data = self.postSerializer.data
        self.assertEqual(data['id'], 1)

    # Test to ensure the text field is correct
    def test_post_serializer_has_correct_text(self):
        data = self.postSerializer.data
        self.assertEqual(data['text'], "My fake post message")

    # Clean up
    def tearDown(self):
        Post.objects.all().delete()
        User.objects.all().delete()




# This class tests the Comment Serializer
class CommentSerializerTests(TestCase):
    user = None
    comment = None
    commentSerializer = None

    # Create instance of Comment model
    def setUp(self):
        self.user = User.objects.create_user(username='jpage', email='jpage@zep.com', first_name='Jimmy', last_name='Page', password='zosozoso')
        self.post = Post.objects.create(text="My fake post message", createdon=make_aware(datetime.datetime.now()), createdby=self.user)
        self.comment = Comment.objects.create(comment="My fake comment", createdon=make_aware(datetime.datetime.now()), createdby=self.user, post=self.post)
        self.commentSerializer = CommentSerializer(instance=self.comment)

    # Test to ensure all fields are present in the serializer
    def testcomment_serializer_has_correct_fields(self):
        data = self.commentSerializer.data
        self.assertEqual(set(data.keys()), set(['id', 'comment', 'createdon', 'createdby', 'post']))

    # Test to ensure the id field is correct
    def test_comment_serializer_has_correct_id(self):
        data = self.commentSerializer.data
        self.assertEqual(data['id'], 1)        

    # Test to ensure the comment field is correct
    def test_comment_serializer_has_correct_fullname(self):
        data = self.commentSerializer.data
        self.assertEqual(data['comment'], "My fake comment")

    # Clean up
    def tearDown(self):
        Comment.objects.all().delete()
        Post.objects.all().delete()
        User.objects.all().delete()
  



  
# This class tests the ChatRoom Serializer
class ChatRoomSerializerTests(TestCase):
    chatroom = None
    chatroomSerializer = None

    # Create instance of ChatRoom model
    def setUp(self):
        self.chatroom = ChatRoom.objects.create(roomname="goodroom")
        self.chatroomSerializer = ChatRoomSerializer(instance=self.chatroom)

    # Test to ensure all fields are present in the serializer
    def test_chatroom_serializer_has_correct_fields(self):
        data = self.chatroomSerializer.data
        self.assertEqual(set(data.keys()), set(['id', 'roomname']))

    # Test to ensure the fullname field is correct
    def test_chatroom_serializer_has_correct_roomname(self):
        data = self.chatroomSerializer.data
        self.assertEqual(data['roomname'], "goodroom")

    # Clean up
    def tearDown(self):
        ChatRoom.objects.all().delete()




# This class tests the Chat Serializer
class ChatSerializerTests(TestCase):
    user = None
    chat = None
    roomanme = None
    chatSerializer = None

    # Create instance of Chat model
    def setUp(self):
        self.user = User.objects.create_user(username='jpage', email='jpage@zep.com', password='zosozoso')
        self.chatroom = ChatRoom.objects.create(roomname="goodroom")
        self.chat = Chat.objects.create(chattext="Hey, what's up?", timestamp=make_aware(datetime.datetime.now()), user=self.user, roomname=self.chatroom)
        self.chatSerializer = ChatSerializer(instance=self.chat)

    # Test to ensure all fields are present in the serializer
    def test_chat_serializer_has_correct_fields(self):
        data = self.chatSerializer.data
        self.assertEqual(set(data.keys()), set(['id', 'chattext', 'timestamp', 'user', 'roomname']))

    # Test to ensure the id field is correct
    def test_chat_serializer_has_correct_id(self):
        data = self.chatSerializer.data
        self.assertEqual(data['id'], 1)        

    # Test to ensure the chattext field is correct
    def test_chat_serializer_has_correct_chattext(self):
        data = self.chatSerializer.data
        self.assertEqual(data['chattext'], "Hey, what's up?")

    # Clean up
    def tearDown(self):
        Chat.objects.all().delete()
        Post.objects.all().delete()
        User.objects.all().delete()
