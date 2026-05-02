from typing import Generic

from django.shortcuts import render


from django.conf import settings
from django.core.mail import send_mail

# """""
# Class-based views:

# Views           = Generic View
# List View       = get a list of records
# DetailView      = get a single record
# CreateView      = create a new record
# DeleteView      = delete an existing record
# UpdateView      = update an existing record
# LoginView       = login


# """"""


# Create your views here.
def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    return render(request, 'pages/contact.html')

