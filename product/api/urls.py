from django.urls import path
from product.api import views

app_name = 'product'

urlpatterns = [
    path('products/', views.ProductModelListAPIView.as_view(), name = "products"),

]