from rest_framework import viewsets
from .serilizer import ProductSerializer
from .models import Product
from rest_framework import filters


class ProductViewSet(viewsets.ModelViewSet):
 
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [filters.SearchFilter , filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['price']