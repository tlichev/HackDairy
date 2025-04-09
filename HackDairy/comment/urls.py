# urls.py
# comments/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:theme_id>/', views.comment_create, name='comment_create'),
    path('edit/<int:pk>/', views.comment_edit, name='comment_edit'),
    path('delete/<int:pk>/', views.comment_delete, name='comment_delete'),
]
