from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.

class HomeView(ListView):
    template_name = "liveappTemp/index.html"
    
    def get(self, request):
        blogs = BlogPost.objects.all()
        
        context = {
            'blogs':blogs
        }
        
        return render(request, self.template_name,context)