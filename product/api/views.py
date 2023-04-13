from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from product.models import ProductModel, FavoriteProductModel, ViewNumberModel, LikeModel, CommentModel
from product.api.serializers import (
    ProductModelListSerializer, ProductModelCreateSerializer,
    FavoriteModelListSerializer, FavoriteModelCreateSerializer, FavoriteModelUpdateSerializer,
    ViewNumberModelListSerializer, ViewNumberModelCreateSerializer, ViewNumberModelUpdateSerializer,
    LikeModelListSerializer, LikeModelCreateSerializer, LikeModelUpdateSerializer,
    CommentModelListSerializer, CommentModelCreateSerializer, CommentModelUpdateSerializer
)


class ProductModelListAPIView(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelListSerializer

class ProductModelCreateAPIView(CreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelCreateSerializer

class ProductModelUpdateAPIView(RetrieveUpdateAPIView):
    queryset = ProductModel.objects.all()
    lookup_field = "id"
    serializer_class = ProductModelCreateSerializer

class ProductModelDestroyAPIView(RetrieveDestroyAPIView):
    queryset = ProductModel.objects.all()
    lookup_field = "id"
    serializer_class = ProductModelListSerializer


class FavoriteModelListAPIView(ListAPIView):
    queryset = FavoriteProductModel.objects.all()
    serializer_class = FavoriteModelListSerializer

class FavoriteModelCreateAPIView(CreateAPIView):
    queryset = FavoriteProductModel.objects.all()
    serializer_class = FavoriteModelCreateSerializer

class FavoriteModelUpdateView(RetrieveUpdateAPIView):
    queryset = FavoriteProductModel.objects.all()
    lookup_field = "id"
    serializer_class = FavoriteModelUpdateSerializer

class FavoriteModelDestroyAPIView(RetrieveDestroyAPIView):
    queryset = FavoriteProductModel.objects.all()
    lookup_field = "id"
    serializer_class = FavoriteModelListSerializer


class ViewNumberModelListAPIView(ListAPIView):
    queryset = ViewNumberModel.objects.all()
    serializer_class = ViewNumberModelListSerializer

class ViewNumberModelCreateAPIView(CreateAPIView):
    queryset = ViewNumberModel.objects.all()
    serializer_class = ViewNumberModelCreateSerializer

class ViewNumberModelUpdateAPIView(RetrieveUpdateAPIView):
    queryset = ViewNumberModel.objects.all()
    lookup_field = "id"
    serializer_class = ViewNumberModelUpdateSerializer

class ViewNumberModelDestroyAPIView(RetrieveDestroyAPIView):
    queryset = ViewNumberModel.objects.all()
    lookup_field = "id"
    serializer_class = ViewNumberModelListSerializer


class LikeModelListAPIView(ListAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeModelListSerializer

class LikeModelCreateAPIView(CreateAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeModelCreateSerializer

class LikeModelUpdateAPIView(RetrieveUpdateAPIView):
    queryset = LikeModel.objects.all()
    lookup_field = "id"
    serializer_class = LikeModelUpdateSerializer

class LikeModelDestroyAPIView(RetrieveDestroyAPIView):
    queryset = LikeModel.objects.all()
    lookup_field = "id"
    serializer_class = LikeModelListSerializer


class CommentModelListAPIView(ListAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentModelListSerializer

class CommentModelCreateAPIView(CreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentModelCreateSerializer

class CommentModelUpdateAPIView(RetrieveUpdateAPIView):
    queryset = CommentModel.objects.all()
    lookup_field = "id"
    serializer_class = CommentModelUpdateSerializer

class CommentModelDestroyAPIView(RetrieveDestroyAPIView):
    queryset = CommentModel.objects.all()
    lookup_field = 'id'    
    serializer_class = CommentModelListSerializer
