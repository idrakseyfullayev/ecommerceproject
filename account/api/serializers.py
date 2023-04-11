from rest_framework import serializers
from account.models import Account
from django.contrib.auth.password_validation import validate_password

class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        # exclude = ("password",)
        fields = "__all__"

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




    



    

