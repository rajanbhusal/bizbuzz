from django.db import models
from django.contrib.auth.models import User
import uuid
from users.models import Profile
# Create your models here.


class Post(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    post_image = models.ImageField(null=True, blank=True)
    likes = models.IntegerField(default=0, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False, unique=True)

    @property
    def getLikes(self):
        return self.likes

    def __str__(self):
        return self.description[0:10] + '...'

    class Meta:
        ordering = ['-created']


class Comment(models.Model):
    commenter = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    commented_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    comment_image = models.ImageField(null=True, blank=True)
    likes = models.IntegerField(default=0, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False, unique=True)

    def __str__(self):
        return self.description[0:10] + '...'


class Like(models.Model):
    liked_by = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    liked_post = models.ForeignKey(
        Post, on_delete=models.SET_NULL, null=True, blank=True)
