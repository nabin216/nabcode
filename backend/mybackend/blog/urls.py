from django.urls import path
from .views import blog_list_create_view, blog_detail_view, comment_list_create_view

urlpatterns = [
    path('blogs/', blog_list_create_view, name='blog-list-create'),
    path('blogs/<int:pk>/', blog_detail_view, name='blog-detail'),
    path('blogs/<int:blog_pk>/comments/', comment_list_create_view, name='comment-list-create'),
]