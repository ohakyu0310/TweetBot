# twitter_api_client.py
import tweepy
from posts.models import TwitterAuth
from decouple import config


def post_to_twitter(text: str) -> dict:
    creds = TwitterAuth.objects.first()
    if not creds:
        return {'success': False, 'error': 'No credentials'}

    try:
        client = tweepy.Client(
            consumer_key=config('TWITTER_CONSUMER_KEY'),
            consumer_secret=config('TWITTER_CONSUMER_SECRET'),
            access_token=creds.access_token,
            access_token_secret=creds.access_token_secret
        )
        tweet = client.create_tweet(text=text)
        return {'success': True, 'id': tweet.data.get('id')}
    except Exception as e:
        return {'success': False, 'error': str(e)}
