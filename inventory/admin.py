from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'category', 'price', 'stock', 'min_stock', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('sku', 'name')
    list_editable = ('price', 'stock', 'is_active')