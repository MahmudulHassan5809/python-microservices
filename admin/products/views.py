from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets,mixins,status


from products.models import Product
from products.serializers import ProductSerializer

from .producer import publish

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        publish('product_list', serializer.data)
        return Response(serializer.data)