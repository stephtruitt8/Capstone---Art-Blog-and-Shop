from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.

def shop_view(request):
    return render(request, 'shop/shop.html')

class ProductListView(ListView):
    model = Product
    template_name = 'shop/shop.html'
    context_object_name = 'products'
    created_at = '-created_at'