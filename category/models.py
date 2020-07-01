from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.contrib import admin
from django.db.models import Count


# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=120,default='')
    

    def item_count(self):
        return Category.objects.annotate(number_of_items=Count('product')).get(id=self.pk).number_of_items # annotate the queryset

    def __str__(self):
        return self.name


