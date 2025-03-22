from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import *
from django.contrib import messages  
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
        return render(request, self.template_name, context) 
    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)

            messages.success(request, "Thank you, your message was sent successfully!") #Add success message

            return redirect('home')

        # If it's not a POST request, just render the page with the blog posts
        posts = BlogPost.objects.all()
        latest_post = BlogPost.objects.order_by('-created_at').first()

        context = {
            'posts': posts,
            'latest_post': latest_post,
        }

        return render(request, self.template_name, context)