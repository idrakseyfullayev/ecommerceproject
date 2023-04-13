from django.db import models
from account.models import Account


# Create your models here.

class ProductModel(models.Model):
    name = models.CharField(max_length=1000)
    photo = models.ImageField(blank=True, null=True, upload_to="product_photos", default="https://p.kindpng.com/picc/s/79-798754_hoteles-y-centros-vacacionales-dish-placeholder-hd-png.png")
    price = models.FloatField()
    about = models.TextField(blank=True, null=True)
    views_number = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
    

class FavoriteProductModel(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="user_favorites")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="product_favorites")

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"

    def __str__(self) -> str:
        return self.user.username + "|" + self.product.name    


class ViewNumberModel(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_viewnumbers')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="product_viewnumbers")

    class Meta:
        verbose_name = "View number"
        verbose_name_plural = "View numbers"

    def __str__(self) -> str:
        return self.user.username + "|" + self.product.name
    

class LikeModel(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="user_likes")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="product_likes")

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self) -> str:
        return self.user.username + "|" + self.product.name


class CommentModel(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="user_comments")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="product_comments")
    comment = models.TextField()
    pub_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ("-id",)

    def __str__(self) -> str:
        return self.user.username + "|" + self.product.name    



    
