from django.urls import path
from base.views import HomePage

# URL for login/signup page
urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]