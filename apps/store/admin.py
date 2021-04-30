from django.contrib import admin

from .models import Category, Product, ProductImage, ProductReview

# Register your models here.
admin.site.register(ProductImage)
admin.site.register(ProductReview)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'slug', 'description', 'price')
