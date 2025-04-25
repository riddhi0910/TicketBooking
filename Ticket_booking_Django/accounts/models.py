# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.username