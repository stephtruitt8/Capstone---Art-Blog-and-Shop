


def cart_count(request):
    cart = request.session.get("cart", {})

    total_items = 0

    for quantity in cart.values():
        total_items += quantity

    return {
        "cart_count": total_items
    }