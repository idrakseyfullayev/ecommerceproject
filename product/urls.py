from django.urls import path, include
from product import views

app_name = 'product'

urlpatterns = [
    path('detail/<int:id>/', views.DetailView.as_view(), name='detail'),
    path('basket/', views.BasketView.as_view(), name ="basket"),
    path('favorite_delete/<int:id>/', views.favorite_delete, name="favorite_delete"),
]

