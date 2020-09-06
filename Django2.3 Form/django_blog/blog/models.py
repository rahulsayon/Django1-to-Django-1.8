from django.db import models

from django.conf import settings

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
    
    