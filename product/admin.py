from django.contrib import admin

# Register your models here.

from product.models import ProductModel, ViewNumberModel, CommentModel, FavoritProductModel

admin.site.register(ProductModel)
admin.site.register(ViewNumberModel)
admin.site.register(CommentModel)
admin.site.register(FavoritProductModel)

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     pass


