from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from ..themes.models import Theme


class Comment(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.theme.title}'

    class Meta:
        ordering = ['created_date']


# comments/admin.py
from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'theme', 'created_date', 'text_preview')
    list_filter = ('created_date', 'author')
    search_fields = ('text', 'theme__title', 'author__username')

    def text_preview(self, obj):
        return obj.text[:50] + ('...' if len(obj.text) > 50 else '')

    text_preview.short_description = 'Comment Text'