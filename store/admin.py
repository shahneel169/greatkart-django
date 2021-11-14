from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price', 'stock', 'is_available', 'modified_date', 'created_date')
    readonly_fields = ('created_date', 'modified_date')
    ordering = ('-created_date',)
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product,ProductAdmin)