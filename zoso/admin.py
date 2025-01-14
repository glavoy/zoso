from django.contrib import admin
from .models import *

# Register all models on the Admin site
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Chat)
admin.site.register(ChatRoom)