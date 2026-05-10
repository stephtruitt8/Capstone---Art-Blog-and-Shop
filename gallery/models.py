from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class Artwork(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='artworks/', null=True, blank=True)
    video_url = EmbedVideoField(null=True, blank=True)

    def __str__(self):
        return self.title