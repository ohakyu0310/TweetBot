from django.urls import path
from . import views

from .views import (
    PostContentListView,
    PostContentCreateView,
    PostContentUpdateView,
    PostContentDeleteView,
    PostScheduleCreateView,
    PostScheduleListView,
)

urlpatterns = [
    path('posts/', PostContentListView.as_view(), name='post_list'),
    path('posts/new/', PostContentCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', PostContentUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', PostContentDeleteView.as_view(), name='post_delete'),

    # 予約投稿
    path('posts/schedule/', PostScheduleListView.as_view(), name='schedule_list'),
    path('posts/schedule/new/', PostScheduleCreateView.as_view(), name='schedule_create'),

    # 管理用Twitter投稿（手動実行）
    path('admin/test-twitter-post/<int:auth_id>/', views.test_post_to_twitter, name='test_tweet'),
]
