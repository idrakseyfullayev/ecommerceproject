from rest_framework import serializers
from account.models import Account
from django.contrib.auth.password_validation import validate_password
from product.models import FavoriteProductModel, ProductModel
# from product.api.serializers import FavoriteModelListSerializer


class FavoriteModelListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset = Account.objects.all(), slug_field="username")
    product = serializers.SlugRelatedField(queryset = ProductModel.objects.all(), slug_field="name")
    class Meta:
        model = FavoriteProductModel
        fields = "__all__"


class AccountListSerializer(serializers.ModelSerializer):
    user_favorites = FavoriteModelListSerializer(many=True,)
    # user_favorites = serializers.SlugRelatedField(queryset = FavoriteProductModel.objects.all(), slug_field="name")
    class Meta:
        model = Account
        exclude = ("password",)
        # fields = "__all__"
        # fields = ("username", 'first_name', 'last_name', 'password', "user_favorites")

class AccountCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True)
    class Meta:
        model = Account
        fields = ("username", 'first_name', 'last_name', 'password')

    def validate(self, data):
        validate_password(data["password"])
        return data    
    
    def create(self, validated_data):
        account = Account.objects.create(
            username = validated_data["username"],
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
        )

        account.set_password(validated_data["password"])

        account.save()
        return account
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance




    



    

