from django.db import models
from product.models import Product
from django.urls import reverse
from django.conf import settings
from django.utils.html import mark_safe

# Create your models here.
class Albom(models.Model):
    name = models.CharField(max_length=120)
    products = models.ManyToManyField(to=Product)

    def __str__(self):
        return self.name

    def albom_url(self, *args, **kargs):
        if(self.name == ''):
            return 'name is none'
        domain = settings.BASE_URL
        show_albom_url = reverse('show_albom', args=(self.name,))
        url = domain + show_albom_url
        return mark_safe('<a href="%s">%s</a>' % (url, url))
    albom_url.allow_tags = True

