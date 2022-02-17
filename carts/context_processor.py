from .models import Cart, CartItem
from .views import _cart_id 

def cart_counter(request):
    if 'admin' in request.path:
        return {}

    try:
        cart = Cart.objects.filter(cart_id=_cart_id(request))[:1]
        cartitems = CartItem.objects.filter(cart=cart)
        cart_count = 0

        for cartitem in cartitems:
            cart_count += cartitem.quantity

    except Cart.DoesNotExist:
        cart_count=0

    return dict(cart_count=cart_count)