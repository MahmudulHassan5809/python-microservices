from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets,mixins,status


from products.models import Product
from products.serializers import ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer