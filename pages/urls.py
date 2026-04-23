from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_view, name='root'),
    path('about/', views.about_view, name='about'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('shop/', views.shop_view, name='shop'),
    path('blog/', views.blog_view, name='blog'),
    path('contact/', views.contact_view, name='contact'),


]