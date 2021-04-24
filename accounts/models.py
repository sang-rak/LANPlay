from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    meet_id = models.ForeignKey('meets.Meets', on_delete=models.CASCADE, null=True)

