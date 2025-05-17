from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('creator', 'Creator'),
        ('viewer', 'Viewer'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
