from djongo import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
