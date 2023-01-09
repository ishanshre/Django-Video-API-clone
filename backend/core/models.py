from django.db import models

from accounts.models import Profile
# Create your models here.
class Channel(models.Model):
    class CHANNEL_TYPE(models.TextChoices):
        PUBLIC = "PU", 'Public'
        PRIVATE = "PR", 'Private'

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="channels")
    name = models.CharField(max_length=255)
    channel_type = models.CharField(max_length=2, choices=CHANNEL_TYPE.choices, default=CHANNEL_TYPE.PRIVATE)
    thumbnail = models.ImageField(upload_to="channel/thumbnails", null=True, blank=True)
    banner = models.ImageField(upload_to="channel/banners", null=True, blank=True)
    about = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="channel/content/thumbnail", null=True, blank=True)
    video = models.FileField(upload_to="channel/content/video")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="contents")
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="contents")
    uploaded = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title