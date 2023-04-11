from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from product.models import ProductModel
from product.api.serializers import (
    ProductModelListSerializer,
)



class ProductModelListAPIView(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelListSerializer


