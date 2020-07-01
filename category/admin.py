from django.contrib import admin
from .models import Category

# Register your models here.
#admin.site.register(Category)
from product.models import Product
class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
    readonly_fields = ('image_tag',)

class CategoryCastumAdmin(admin.ModelAdmin):
    list_per_page = 10
    inlines = [ProductInline,]
    readonly_fields = ('item_count', )
    list_display = ('name', 'item_count', )
    list_display_links = ('name',)
    #list_filter  = ('category',)

admin.site.register(Category, CategoryCastumAdmin)