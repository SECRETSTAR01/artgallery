from django.db import models

# Create your models here.
class ArtModel(models.Model):
    art_work = models.ImageField(upload_to="arts/")
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    
