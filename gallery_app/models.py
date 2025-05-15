from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='gallery_covers/')

    def __str__(self):
        return self.title
