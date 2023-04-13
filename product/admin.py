from django.contrib import admin

# Register your models here.

from product.models import ProductModel, ViewNumberModel, CommentModel, FavoriteProductModel, LikeModel

admin.site.register(ProductModel)
admin.site.register(ViewNumberModel)
admin.site.register(CommentModel)
admin.site.register(FavoriteProductModel)
admin.site.register(LikeModel)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     pass


