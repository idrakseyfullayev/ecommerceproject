from django.urls import path
from product.api import views

app_name = 'product'

urlpatterns = [
    path('products/', views.ProductModelListAPIView.as_view(), name = "products"),
    path('product-create/', views.ProductModelCreateAPIView.as_view(), name="product-create"),
    path('product-update/<int:id>/', views.ProductModelUpdateAPIView.as_view(), name="product-update"),
    path('product-destroy/<int:id>/', views.ProductModelDestroyAPIView.as_view(), name="product-destroy"),
    path('favorites/', views.FavoriteModelListAPIView.as_view(), name="favorites"),
    path('favorite-create/', views.FavoriteModelCreateAPIView.as_view(), name="favorite-create"),
    path('favorite-update/<int:id>/', views.FavoriteModelUpdateView.as_view(), name="favorite-update"),
    path('favorite-destroy/<int:id>/', views.FavoriteModelDestroyAPIView.as_view(), name="favorite-destroy"),
    path("view_numbers/", views.ViewNumberModelListAPIView.as_view(), name="view_numbers"),
    path("view_number-create/", views.ViewNumberModelCreateAPIView.as_view(), name="view_number-create"),
    path("view_number-update/<int:id>/", views.ViewNumberModelUpdateAPIView.as_view(), name="view_number-update"),
    path("view_number-destroy/<int:id>/", views.ViewNumberModelDestroyAPIView.as_view(), name="view_number-destroy"),
    path('likes/', views.LikeModelListAPIView.as_view(), name="likes"),
    path('like-create/', views.LikeModelCreateAPIView.as_view(), name="like-create"),
    path('like-update/<int:id>/', views.LikeModelUpdateAPIView.as_view(), name="like-update"),
    path('like-destroy/<int:id>/', views.LikeModelDestroyAPIView.as_view(), name="like-destroy"),
    path('comments/', views.CommentModelListAPIView.as_view(), name="comments"),
    path('comment-create/', views.CommentModelCreateAPIView.as_view(), name="comment-create"),
    path('comment-update/<int:id>/', views.CommentModelUpdateAPIView.as_view(), name="comment-create"),
    path('comment-destroy/<int:id>/', views.CommentModelDestroyAPIView.as_view(), name="comment-create"),
]