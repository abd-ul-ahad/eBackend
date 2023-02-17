# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
from Products.models import Products
from Products.serializers import ProductsSerializer
from rest_framework import generics

# Create your views here.

class ProductsDetailsViewSet(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

    
class ProductsCreateViewSet(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


# Export Statements
products_create_view = ProductsCreateViewSet.as_view()
products_details_view = ProductsDetailsViewSet.as_view()

   
