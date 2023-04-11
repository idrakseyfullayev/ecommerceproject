from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from account.models import Account
from account.api.serializers import (
    AccountListSerializer, AccountCreateSerializer,)

class AccountListAPIView(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountListSerializer

class AccountCreatAPIView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer


class AccountUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    lookup_field = "id"
    serializer_class = AccountCreateSerializer

class AccountDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Account.objects.all()
    lookup_field = "id"
    serializer_class = AccountListSerializer





