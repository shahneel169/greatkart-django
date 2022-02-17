from django.contrib import admin
from .models import Product,Variation

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'price', 'stock', 'is_available', 'modified_date', 'created_date')
    readonly_fields = ('created_date', 'modified_date')
    ordering = ('-created_date',)
    prepopulated_fields = {'slug': ('product_name',)}


class VariationAdmin(admin.ModelAdmin):
    list_display = ('variation_product', 'variation_product_category', 'variation_value', 'is_active')
    list_filter = ('variation_product', 'variation_product_category', 'variation_value')
    list_editable = ('is_active',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Variation,VariationAdmin)