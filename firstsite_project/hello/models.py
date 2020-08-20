from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    body = models.TextField()
    
    def __str__(self):
       return self.title

class BlogComment(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    blog_id = models.ForeignKey(Blog,on_delete = models.CASCADE)