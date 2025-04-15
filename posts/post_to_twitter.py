from django.utils import timezone
from posts.models import PostContent, PostSchedule
from posts.twitter_api_client import post_to_twitter

def run_scheduled_posts():
    now = timezone.now()
    pending = PostSchedule.objects.filter(
        scheduled_time__lte=now,
        is_posted=False,
        content__is_active=True
    )

    for item in pending:
        result = post_to_twitter(item.content.body)
        if result['success']:
            item.is_posted = True
            item.posted_at = now
            item.save()

def run_random_posts():
    item = PostContent.objects.filter(is_active=True).order_by('?').first()
    if item != None:
        post_to_twitter(item.body)
