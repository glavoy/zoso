from django.shortcuts import render
from django.views import View

# Starting page - show signup/login page
class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base/index.html')