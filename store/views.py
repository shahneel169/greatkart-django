from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import Paginator
# Create your views here.

def store(request,category_slug=None):

    if category_slug!=None:
        category = get_object_or_404(Category,slug = category_slug)
        products = Product.objects.filter(category=category,is_available = True).order_by('-created_date')
        paginator = Paginator(products,6) 
        page = request.GET.get("page")
        page_products = paginator.get_page(page)

    else:    
        products = Product.objects.filter(is_available = True).order_by('-created_date')
        paginator = Paginator(products,6) 
        page = request.GET.get("page")
        page_products = paginator.get_page(page)
    
    
   
    context = {
        'products':page_products,
        
    }
    return render(request,'store/store.html', context)



def product_detail(request,category_slug=None,product_slug=None):
    product = get_object_or_404(Product, slug=product_slug)
    in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), product=product).exists()
    context = {
        'product':product,
        'in_cart':in_cart
    }
    return render(request,'store/product_detail.html',context)


def search(request):
    search = request.GET.get("search")
    # search = request.GET["search"]
    print("================",search)
    products = Product.objects.filter(is_available =True, product_name__icontains = search).order_by('-created_date')
    context={
        'products':products
    }
    return render(request,'store/store.html',context)