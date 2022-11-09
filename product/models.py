from distutils.command.upload import upload
from itertools import product
from logging import PlaceHolder
from operator import mod
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100 , verbose_name= _("Product Name") , null=True )
    price = models.DecimalField(max_digits=5 , decimal_places=2 , verbose_name = _("price"))
    image = models.ImageField(upload_to='products/') 

    PRDSlug = models.SlugField(null=True , blank=True , verbose_name=("Product url"))
    
    def save(self, *args , **kwargs):
        if not self.PRDSlug :
            self.PRDSlug = slugify(self.name)
        super(Product , self).save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse('product:product_details', kwargs={'id': self.id})
    
    def __str__(self) :
        return self.name




