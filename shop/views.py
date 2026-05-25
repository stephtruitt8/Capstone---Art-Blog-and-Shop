from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .models import Product, Category


# Main shop page
def shop_view(request):
    query = request.GET.get("q", "")
    category_slug = request.GET.get("category", "")
    print("CATEGORY SLUG:", category_slug)
    selected_stock = request.GET.get("stock", "")
    min_price = request.GET.get("min_price", "")
    max_price = request.GET.get("max_price", "")

    product_list = Product.objects.all()
    categories = Category.objects.all()

    if query:
        product_list = product_list.filter(title__icontains=query)

    if category_slug:
        product_list = product_list.filter(category__slug=category_slug)

    if selected_stock == "in_stock":
        product_list = product_list.filter(stock__gt=0)

    if selected_stock == "sold_out":
        product_list = product_list.filter(stock=0)

    if min_price:
        product_list = product_list.filter(price__gte=min_price)

    if max_price:
        product_list = product_list.filter(price__lte=max_price)

    context = {
        "product_list": product_list,
        "categories": categories,
        "query": query,
        "selected_category": category_slug,
        "selected_stock": selected_stock,
        "min_price": min_price,
        "max_price": max_price,
    }

    return render(request, "shop/shop.html", context)


# Product detail page
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, "shop/product_detail.html", {
        "product": product
    })


# Cart page
def cart_detail(request):
    cart = request.session.get("cart", {})

    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        total += subtotal

        cart_items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal,
        })

    context = {
        "cart_items": cart_items,
        "total": total,
    }

    return render(request, "shop/cart.html", context)


# Add product to cart
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get("cart", {})
    product_id = str(product_id)

    if product.stock <= 0:
        return redirect("shop")

    current_quantity = cart.get(product_id, 0)

    if current_quantity < product.stock:
        cart[product_id] = current_quantity + 1

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("shop")


# Remove whole product from cart
def remove_from_cart(request, product_id):
    cart = request.session.get("cart", {})
    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart_detail")


# Optional: decrease quantity by 1
def decrease_cart_item(request, product_id):
    cart = request.session.get("cart", {})
    product_id = str(product_id)

    if product_id in cart:
        if cart[product_id] > 1:
            cart[product_id] -= 1
        else:
            del cart[product_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart_detail")


# Checkout page
def checkout(request):
    cart = request.session.get("cart", {})

    if not cart:
        return redirect("cart_detail")

    return render(request, "shop/checkout.html")


# Success page
def success(request):
    request.session["cart"] = {}
    request.session.modified = True

    return render(request, "shop/success.html")


# Optional CBVs if you want them later
class ProductListView(ListView):
    model = Product
    template_name = "shop/shop.html"
    context_object_name = "product_list"
    ordering = ["-created_at"]


class ProductDetailView(DetailView):
    model = Product
    template_name = "shop/product_detail.html"
    context_object_name = "product"