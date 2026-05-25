from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_view, name='blog'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
]