from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    
def LoginView(request):
    return render(request, 'accounts/login.html')

def LogoutView(request):
    return render(request, 'accounts/logout.html')

def ProfileView(request):
    return render(request, 'accounts/profile.html') 