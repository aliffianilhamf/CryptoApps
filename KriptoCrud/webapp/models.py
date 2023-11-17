from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Cerita(models.Model):
    judul = models.CharField(max_length=200)
    konten = models.TextField()
    image = models.ImageField(null= True, blank= True, upload_to='image')
    creation_date = models.DateTimeField(auto_now_add= True)
    penulis = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.judul
    
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url