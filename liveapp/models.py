from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=450)
    content = models.TextField()
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject