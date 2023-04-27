from rest_framework import serializers
from product.models import ProductModel, FavoriteProductModel, ViewNumberModel, LikeModel, CommentModel
from account.api.serializers import AccountListSerializer
from account.models import Account

class ProductModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"

class ProductModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ("name", "photo", "price", "about")       


class FavoriteModelListSerializer(serializers.ModelSerializer):
    user = serializers.SlugField()   
    product = serializers.SlugField()
    # user = AccountListSerializer()
    # product = ProductModelListSerializer()
    class Meta:
        model = FavoriteProductModel
        fields = "__all__"

class FavoriteModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProductModel
        fields = "__all__"

class FavoriteModelUpdateSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset = Account.objects.all(), slug_field="username")
    product = serializers.SlugRelatedField(queryset = ProductModel.objects.all(), slug_field="name")
    class Meta:
        model = FavoriteProductModel
        fields = "__all__"


class ViewNumberModelListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset = Account.objects.all(), slug_field="username")
    product = serializers.SlugRelatedField(queryset = ProductModel.objects.all(), slug_field = "name")
    # user = AccountListSerializer()
    # product = ProductModelListSerializer()
    class Meta:
        model = ViewNumberModel
        fields = "__all__"

class ViewNumberModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewNumberModel
        fields = "__all__"

class ViewNumberModelUpdateSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset = Account.objects.all(), slug_field="username")
    product = serializers.SlugRelatedField(queryset = ProductModel.objects.all(), slug_field="name")
    class Meta:
        model = ViewNumberModel
        fields = "__all__"



class LikeModelListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset = Account.objects.all(), slug_field="username")
    product = serializers.SlugRelatedField(queryset = ProductModel.objects.all(), slug_field="name")
    # user = AccountListSerializer()
    # product = ProductModelListSerializer()
    class Meta:
        model = LikeModel
        fields = "__all__"

class LikeModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeModel
        fields = "__all__"

class LikeModelUpdateSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset = Account.objects.all(), slug_field="username")
    product = serializers.SlugRelatedField(queryset = ProductModel.objects.all(), slug_field="name")
    class Meta:
        model = LikeModel
        fields = "__all__"


class CommentModelListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset = Account.objects.all(), slug_field="username")
    product = serializers.SlugRelatedField(queryset = ProductModel.objects.all(), slug_field="name")
    # user = AccountListSerializer()
    # product = ProductModelListSerializer()
    class Meta:
        model = CommentModel
        fields = "__all__"

class CommentModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = "__all__"


class CommentModelUpdateSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset = Account.objects.all(), slug_field="username")
    product = serializers.SlugRelatedField(queryset = ProductModel.objects.all(), slug_field="name")
    class Meta:
        model = CommentModel
        fields = "__all__"
        
        