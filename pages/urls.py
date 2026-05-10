from django.urls import path
from . import views
from .views import about_view, contact_view

urlpatterns = [
    path('', views.about_view, name='root'),
    path('about/', views.about_view, name='about'),

    path('contact/', views.contact_view, name='contact'),
    path('commissions/', views.commissions_view, name='commissions'),



]