from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# class Rooms(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     # title = models.CharField(max_length=10)
#     # content = models.TextField()
#     # created_at = models.DateTimeField(auto_now_add=True)
#     # updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title