from django.contrib import admin
from django.utils.html import format_html
from .models import TwitterAuth, PostContent

@admin.register(PostContent)
class PostContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'body')
    ordering = ('-created_at',)

@admin.register(TwitterAuth)
class TwitterAuthAdmin(admin.ModelAdmin):
    list_display = ('access_token_short', 'created_at', 'test_post_button')

    def access_token_short(self, obj):
        return obj.access_token[:10] + "..."

    access_token_short.short_description = "Access Token"

    def test_post_button(self, obj):
        return format_html(
            '<a class="button" href="{}">テスト投稿</a>',
            f'/admin/test-twitter-post/{obj.pk}/'
        )

    test_post_button.short_description = "テスト投稿"
