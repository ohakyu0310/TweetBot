from django.core.management.base import BaseCommand
from posts.post_to_twitter import run_random_posts

class Command(BaseCommand):
    help = '投稿予約に基づいてTwitterに投稿します'

    def handle(self, *args, **kwargs):
        run_random_posts()