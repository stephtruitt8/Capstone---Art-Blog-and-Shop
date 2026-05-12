from django import forms
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    project_type = forms.ChoiceField(choices=[
        ("Illustration", "Illustration"),
        ("Character Design", "Character Design"),
        ("Story Art", "Story Art"),
        ("Animation", "Animation"),
        ("Other", "Other"),
    ])
    interest = forms.ChoiceField(choices=[
        ("Commission Work", "Commission Work"),
        ("Buying Art", "Buying Art"),
        ("Brand Collaboration", "Brand Collaboration"),
        ("General Question", "General Question"),
    ])
    message = forms.CharField(widget=forms.Textarea)
    referral = forms.ChoiceField(choices=[
        ("Instagram", "Instagram"),
        ("Behance", "Behance"),
        ("Facebook", "Facebook"),
        ("Friend / Referral", "Friend / Referral"),
        ("Other", "Other"),
    ])