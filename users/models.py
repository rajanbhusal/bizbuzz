from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    profile_image = models.ImageField(
        default="avatar.jpg", null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    college = models.CharField(max_length=200, null=True, blank=True)
    instagram_id = models.CharField(max_length=200, null=True, blank=True)
    twitter_id = models.CharField(max_length=200, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='sender')
    receipient = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    text_image = models.ImageField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)

    def __str__(self):
        return self.description[0:10]+'...'

    class Meta:
        ordering = ['-created']
