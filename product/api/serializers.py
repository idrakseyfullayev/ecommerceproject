from rest_framework import serializers
from product.models import ProductModel

class ProductModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"

