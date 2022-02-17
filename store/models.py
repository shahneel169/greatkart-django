from django.db import models
from django.urls import reverse
from category.models import Category

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug         = models.SlugField(max_length=100, unique=True)
    description  = models.TextField(blank=True)
    price        = models.IntegerField()
    images       = models.ImageField(upload_to='photoes/products')
    stock        = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category     = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date= models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product-detail', args=[self.category.slug,self.slug])

    def __str__(self):
        return self.product_name

choices = [
    ('color','color'),
    ('size','size')
]


class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager,self).filter(variation_product_category='color',is_active=True)

    def sizes(self):
        return super(VariationManager,self).filter(variation_product_category='size',is_active=True)

class Variation(models.Model):
    variation_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_product_category = models.CharField(max_length=100, choices = choices)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_product.product_name + ' ' + self.variation_product_category+'='+self.variation_value
