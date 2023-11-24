from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Cerita(models.Model):
    judul = models.CharField(max_length=200)
    konten = models.TextField()
    creation_date = models.DateTimeField(auto_now_add= True)
   
    
    def __str__(self):
        return self.judul
    