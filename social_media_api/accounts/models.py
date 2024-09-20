from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Other fields...
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change this name as needed
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Change this name as needed
        blank=True,
    )