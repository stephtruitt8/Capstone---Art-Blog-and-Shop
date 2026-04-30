from django.shortcuts import render


from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def about_view(request):
    return render(request, 'pages/about.html')

def gallery_view(request):
    return render(request, 'pages/gallery.html')

# // All links to the different galleries will be added here, and the individual gallery pages will be created as well. For now, they will just render the gallery template.

def illustrations_view(request):
    return render(request, 'pages/illustrations.html')

def sketches_view(request):
    return render(request, 'pages/sketches.html')

def story_art_view(request):
    return render(request, 'pages/story_art.html')


def shop_view(request):
    return render(request, 'pages/shop.html')


def contact_view(request):
    return render(request, 'pages/contact.html')

