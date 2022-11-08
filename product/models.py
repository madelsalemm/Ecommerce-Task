from distutils.command.upload import upload
from itertools import product
from logging import PlaceHolder
from operator import mod
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

class Product(models.Model):
    PRDName = models.CharField(max_length=100 , verbose_name= _("Product Name") , null=True )
    PRDCost = models.DecimalField(max_digits=5 , decimal_places=2 , verbose_name = _("Cost"))

    PRDSlug = models.SlugField(null=True , blank=True , verbose_name=("Product url"))
    
    def save(self, *args , **kwargs):
        if not self.PRDSlug :
            self.PRDSlug = slugify(self.PRDName)
        super(Product , self).save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse('product:product_details', kwargs={'slug': self.PRDSlug})
    
    def __str__(self) :
        return self.PRDName
    



