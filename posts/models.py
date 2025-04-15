from django.db import models

class PostContent(models.Model):
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # 投稿対象にするか

class PostSchedule(models.Model):
    content = models.ForeignKey(PostContent, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
    is_posted = models.BooleanField(default=False)
    posted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        ordering = ['scheduled_time']

class TwitterAuth(models.Model):
    access_token = models.CharField(max_length=255)
    access_token_secret = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
