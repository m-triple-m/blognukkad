from django.db import models
from martor.models import MartorField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=30)
    description = MartorField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title