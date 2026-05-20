from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_view, name='shop'),

    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    path('cart/', views.cart_detail, name='cart_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.success, name='success'),
]