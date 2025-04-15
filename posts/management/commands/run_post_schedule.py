from django.core.management.base import BaseCommand
from posts.post_to_twitter import run_scheduled_posts

class Command(BaseCommand):
    help = '登録されているポストをランダムにTwitterに投稿します'

    def handle(self, *args, **kwargs):
        run_scheduled_posts()
