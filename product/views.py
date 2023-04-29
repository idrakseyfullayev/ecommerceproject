from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, get_list_or_404
from product.models import ProductModel, ViewNumberModel, LikeModel, CommentModel, FavoriteProductModel
from django.views import generic
from django.db.models import Q

class IndexView(generic.View):
    def get(self, request, *args, **kwargs):
        products = ProductModel.objects.all()
        user_favorites = []
        if request.user.is_authenticated:
            for i in request.user.user_favorites.all():
                user_favorites.append(i.product)  

        query = request.GET.get("query")

        if query:
            products = ProductModel.objects.filter(Q(name__contains = query))
    
        context ={
            'products': products,
            'user_favorites': user_favorites
        }

        return render(request, 'index.html', context)
    
    def post(self, request, *args, **kwargs):
        productid = request.POST.get("productid")
        product = ProductModel.objects.get(id=productid)
        if request.user.is_authenticated:
            if not FavoriteProductModel.objects.filter(user=request.user, product=product):
                FavoriteProductModel.objects.create(user=request.user, product=product)

        return redirect('index')
    
    

class DetailView(generic.View):
    def get(self, request, id, *args, **kwargs):
        product = get_object_or_404(ProductModel, id=id)
        user_favorites = []
        if request.user.is_authenticated:
            for i in request.user.user_favorites.all():
                user_favorites.append(i.product)

        if request.user.is_authenticated:
            if not ViewNumberModel.objects.filter(user=request.user, product=product):
                ViewNumberModel.objects.create(user=request.user, product=product)
                product.views_number += 1
                product.save()
        else:
            product.views_number += 1
            product.save()


        context = {
            'product': product,
            'user_favorites': user_favorites
        }

        return render(request, 'detail.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('choice') == "like":
            productid = request.POST.get("productid")
            product = ProductModel.objects.get(id=productid)

            if not LikeModel.objects.filter(user=request.user, product=product):
                LikeModel.objects.create(user=request.user, product=product)
        
            return redirect("product:detail", productid)
        
        elif request.POST.get("choice") == "basket":
            productid = request.POST.get("productid")
            product = ProductModel.objects.get(id=productid)

            if request.user.is_authenticated:
                if not FavoriteProductModel.objects.filter(user=request.user, product=product):
                    FavoriteProductModel.objects.create(user=request.user, product=product)

            return redirect('product:detail', productid)        
        
        elif request.POST.get('choice') == "comment":
            productid = request.POST.get("productid")
            product = ProductModel.objects.get(id=productid)
            comment = request.POST.get("comment")
            CommentModel.objects.create(user=request.user, product=product, comment=comment)

            return redirect("product:detail", productid)

        
class BasketView(generic.View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_favorites = request.user.user_favorites.order_by("-id")
            query = request.GET.get('query')

            if query:
                user_favorites = user_favorites.filter(Q(product__name__contains = query))

            context = {
                "user_favorites": user_favorites
            }
            
            return render(request, 'basket.html', context)
        else:
            return render(request, 'basket.html') 


def favorite_delete(request, id):
    user_favorite = FavoriteProductModel.objects.get(user=request.user, product_id=id)
    user_favorite.delete()
    return redirect('product:basket')

