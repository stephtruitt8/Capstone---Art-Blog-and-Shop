from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path('gallery/illustrations/', views.illustrations_view, name='illustrations'),
    path('gallery/sketches/', views.sketches_view, name='sketches'),
    path('gallery/story-art/', views.story_art_view, name='story_art'),
]