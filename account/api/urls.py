from django.urls import path
from account.api import views

app_name = "account"

urlpatterns = [
    path('accounts/', views.AccountListAPIView.as_view(), name='accounts'),
    path('account-create/', views.AccountCreatAPIView.as_view(), name="account-create"),
    path("account-update/<int:id>/", views.AccountUpdateAPIView.as_view(), name="account-update"),
    path("account-destroy/<int:id>/", views.AccountDestroyAPIView.as_view(), name="account-destroy"),

]