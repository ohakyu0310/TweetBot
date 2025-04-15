from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import PostContent, PostSchedule
from .forms import PostContentForm, PostScheduleForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import TwitterAuth
from decouple import config
import tweepy

class PostContentListView(ListView):
    model = PostContent
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


class PostContentCreateView(CreateView):
    model = PostContent
    form_class = PostContentForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_list')


class PostContentUpdateView(UpdateView):
    model = PostContent
    form_class = PostContentForm
    template_name = 'posts/post_form.html'
    success_url = reverse_lazy('post_list')


class PostContentDeleteView(DeleteView):
    model = PostContent
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

def test_post_to_twitter(request, auth_id):
    auth_obj = get_object_or_404(TwitterAuth, pk=auth_id)

    # 環境変数などからアプリのキーを取得（安全性重視）
    try:
        client = tweepy.Client(
            consumer_key=config('TWITTER_CONSUMER_KEY'),
            consumer_secret=config('TWITTER_CONSUMER_SECRET'),
            access_token=auth_obj.access_token,
            access_token_secret=auth_obj.access_token_secret
        )

        response = client.create_tweet(text="イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤イグッ❤")
        messages.success(request, f"投稿成功！Tweet ID: {response.data.get('id')}")

    except Exception as e:
        messages.error(request, f"投稿失敗: {str(e)}")

    return HttpResponseRedirect('/admin/posts/twitterauth/')

class PostScheduleListView(ListView):
    model = PostSchedule
    template_name = 'posts/schedule_list.html'
    context_object_name = 'schedules'

class PostScheduleCreateView(CreateView):
    model = PostSchedule
    form_class = PostScheduleForm
    template_name = 'posts/schedule_form.html'
    success_url = reverse_lazy('schedule_list')