from django.urls import path, include
from product import views

app_name = 'product'

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('detail/<int:id>/', views.DetailView.as_view(), name='detail'),
]

