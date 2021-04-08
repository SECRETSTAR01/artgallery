from django.db import models

# Create your models here.
class ArtModel(models.Model):
    art_work = models.FileField()
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)

    
