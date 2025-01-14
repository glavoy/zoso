from django.db import models
from django.utils import timezone

# Using the buil-in Django authentication
from django.contrib.auth.models import User

# These are used to automatically create a default profile
# after a user signs up
from django.db.models.signals import post_save
from django.dispatch import receiver


# Model for the user profile
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user',
                                related_name='profile', on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30, blank=True, null=True)
    about = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    profilepic = models.ImageField(upload_to='profile_pics',
                                   default='profile_pics/default.png')
    contacts = models.ManyToManyField(
        User, blank=True, related_name='contacts')

    def __str__(self):
        return self.fullname



# Model for a Post
class Post(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='post_pics', blank=True, null=True)
    createdon = models.DateTimeField(default=timezone.now)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text



# Model for comments on a post
class Comment(models.Model):
    comment = models.TextField()
    createdon = models.DateTimeField(default=timezone.now)
    createdby = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.comment



# Model for the Chat room
class ChatRoom(models.Model):
    roomname = models.CharField(max_length=200)

    def __str__(self):
        return self.roomname



# Model for chat
class Chat(models.Model):
    chattext = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roomname = models.ForeignKey('ChatRoom', on_delete=models.CASCADE)

    def __str__(self):
        return self.chattext



# Create a default user profile
# User can edit this later
# https://docs.djangoproject.com/en/4.0/topics/signals/
# This function is called every time a new user is created
# It will create a default Profile with the default image
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Save the default user profile
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
