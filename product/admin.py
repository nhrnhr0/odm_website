from django.contrib import admin
from .models import Product

class ProductCastumAdmin(admin.ModelAdmin):
    #fields = ('name',)
    fields = ( 'name', 'image', 'image2', 'category', 'image_tag', 'image2_tag')
    readonly_fields = ('image_tag','image2_tag')
    list_display = ('name', 'category', 'image_tag', 'image2_tag')
    list_display_links = ('name',)
    list_filter  = ('category',)

admin.site.register(Product, ProductCastumAdmin)
