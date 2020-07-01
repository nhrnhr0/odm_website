from django.contrib import admin
from .models import Albom
# Register your models here.
#admin.site.register(Albom)
#from category.admin import ProductInline
 
class ProductInline(admin.TabularInline):
    model = Albom.products.through
    extra = 0
    #readonly_fields = ('image_tag', )

class AlbomCastumAdmin(admin.ModelAdmin):
    list_display = ('name', 'albom_url',)
    readonly_fields = ('albom_url', )
    filter_horizontal = ('products',)
    list_per_page = 10
    #readonly_fields = ('image_tag', )
    inlines = [ProductInline,]
    pass

admin.site.register(Albom, AlbomCastumAdmin )

"""
class albomProductInline(admin.TabularInline):
    model = Albom.products.through
    fields = ['row_name']
    readonly_fields = ['row_name']
    def row_name(self, instance):
        print('name:')
        print(dir(instance.product_id))
        print(instance.product_id)
        print(instance.product)
        #print('name:', instance.dir())
        return instance.product.name
    row_name.short_description = 'row name'


    #readonly_fields = ['name']

class AlbomCastumAdmin(admin.ModelAdmin):
    inlines = [albomProductInline,]
    exclude = ('products',)
admin.site.register(Albom, AlbomCastumAdmin )
"""