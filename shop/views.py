from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.

def shop_view(request):
    product_list = Product.objects.all()

    return render(request, 'shop/shop.html', {
        'product_list': product_list
    })

# class ProductListView(ListView):
#     model = Product
#     template_name = 'shop/shop.html'
#     context_object_name = 'products'
#     created_at = '-created_at'