from django.db import models
from django.conf import settings

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='images', default="")
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
