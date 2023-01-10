"""
Action app models consist of models that is tracks user actions such as like, unlike, follow, et cetera
"""

from django.db import models

from accounts.models import Profile
from core.models import Channel, Content
# Create your models here.
class Subscription(models.Model):
    is_subscribed = models.BooleanField(default=False)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="subscribe_to")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="subscribed_by")
    subscribed_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['-subscribed_date']),]
        ordering = ['-subscribed_date']
    
    def __str__(self):
        return f"{self.profile.user.username.title()} subscribed @{self.channel.name}"


class Like(models.Model):
    is_liked = models.BooleanField(default=False)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="likes")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="liked_videos")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.user.username.title()} likes {self.content.title}"


class Dislike(models.Model):
    is_disliked = models.BooleanField(default=False)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="dislikes")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="disliked_videos")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profile.user.username.title()} dislikes {self.content.title}"


