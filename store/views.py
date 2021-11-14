from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import Category

# Create your views here.

def store(request,category_slug=None):

    if category_slug!=None:
        category = get_object_or_404(Category,slug = category_slug)
        products = Product.objects.filter(category=category,is_available = True)

    else:    
        products = Product.objects.filter(is_available = True).order_by('-created_date')
    
    
   
    context = {
        'products':products,
        
    }
    return render(request,'store/store.html', context)



def product_detail(request,category_slug=None,product_slug=None):
    product = get_object_or_404(Product, slug=product_slug)
    context = {
        'product':product
    }
    return render(request,'store/product_detail.html',context)
