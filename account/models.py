from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    photo = models.ImageField(blank=True, null=True, upload_to='account_photos/')

    