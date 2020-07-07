from django.db import models
from django.conf import settings
from category.models import Category
from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import gettext as _
from django.conf import settings
import os

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=120, default='', blank=True, null=True, verbose_name=_('name'))
    image = models.ImageField(upload_to='desktop', verbose_name='image', default  = 'default.jpg')
    image2 = models.ImageField(upload_to='mobile', verbose_name='image 2',default=  'default.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)


    def image_tag(self):
        #print(image)
        return mark_safe('<img src="%s" width="150" height="150" />' % (settings.MEDIA_URL + self.image.name))

    def image2_tag(self):
        return mark_safe('<img src="%s" width="103" height="224" />' % (settings.MEDIA_URL + self.image2.name))

    def __str__(self):
        name = ''
        if self.name == None:
            name = 'no name'
        else:
            name = self.name
        return self.category.name + '\t|\t' + name

    image_tag.short_description = 'Desktop Image'
    image2_tag.short_description = 'Mobile Image'
    #image_tag.allow_tags = True







