from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    name_first = models.CharField(max_length=20)
    name_last = models.CharField(max_length=25)
    cell_phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=500, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/defaultimage.png")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name_first +' '+ self.name_last)


class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, default="")
    description = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.description)
