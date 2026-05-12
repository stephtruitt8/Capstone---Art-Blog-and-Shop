from typing import Generic

from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives, send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm

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
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            project_type = form.cleaned_data["project_type"]
            interest = form.cleaned_data["interest"]
            message = form.cleaned_data["message"]
            referral = form.cleaned_data["referral"]

            full_name = f"{first_name} {last_name}"

            html_message = render_to_string(
                "emails/contact.html",
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "full_name": full_name,
                    "email": email,
                    "project_type": project_type,
                    "interest": interest,
                    "message": message,
                    "referral": referral,
                }
            )

            plain_message = f"""
New contact form submission

Name: {full_name}
Email: {email}

Project Type: {project_type}
Interested In: {interest}
Referral: {referral}

Message:
{message}
"""

            email_message = EmailMultiAlternatives(
                subject="New BartoArts Contact Form Submission",
                body=plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.DEFAULT_FROM_EMAIL],
                reply_to=[email],
            )

            email_message.attach_alternative(html_message, "text/html")
            email_message.send()

            return redirect("contact")

    else:
        form = ContactForm()

    return render(request, "pages/contact.html", {"form": form})

def commissions_view(request):
    return render(request, 'pages/commissions.html')