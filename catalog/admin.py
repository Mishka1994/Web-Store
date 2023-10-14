from django.contrib import admin

from catalog.models import Category, Product, BlogPost, Version


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category_product')
    list_filter = ('category_product',)
    search_fields = ('name', 'description',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'is_published',)
    list_filter = ('is_published',)
    search_fields = ('title', 'slug', 'content',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_number', 'name_version', 'product', 'current_version_indicator')
    list_filter = ('product', 'current_version_indicator')
