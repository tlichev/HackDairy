from django.contrib import admin
from .models import Theme

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'created_date')
    list_filter = ('created_date', 'creator')
    search_fields = ('title', 'subtitle', 'content')