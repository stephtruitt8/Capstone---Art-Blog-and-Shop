from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def about_view(request):
    return render(request, 'pages/about.html')

def gallery_view(request):
    return render(request, 'pages/gallery.html')

def shop_view(request):
    return render(request, 'pages/shop.html')

def blog_view(request):
    return render(request, 'pages/blog.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email to site owner
            send_mail(
                f'New Contact Form Submission from {name}',
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            return render(request, 'pages/contact_success.html')
    else:
        form = ContactForm()
    
    return render(request, 'pages/contact.html', {'form': form})