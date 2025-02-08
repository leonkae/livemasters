from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.

class HomeView(ListView):
    template_name = "liveappTemp/index.html"
    
    def get(self, request):
        posts = BlogPost.objects.all()
        latest_post = BlogPost.objects.order_by('-created_at').first()
        
        context = {
            'posts':posts,
            'latest_post':latest_post
        }
        
        return render(request, self.template_name,context)