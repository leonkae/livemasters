from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

class HomeView(ListView):
    template_name = "liveappTemp/index.html"
    
    def get(self, request):
        
        context = {
            
        }
        
        return render(request, self.template_name,context)