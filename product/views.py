from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, get_list_or_404
from product.models import ProductModel, ViewNumberModel, LikeModel, CommentModel
from django.views import generic

class IndexView(generic.View):
    def get(self, request, *args, **kwargs):
        products = ProductModel.objects.all()
    
        context ={
            'products': products
        }

        return render(request, 'index.html', context)
    

class DetailView(generic.View):
    def get(self, request, id, *args, **kwargs):
        product = get_object_or_404(ProductModel, id=id)

        if request.user.is_authenticated:
            if not ViewNumberModel.objects.filter(user=request.user, product=product):
                ViewNumberModel.objects.create(user=request.user, product=product)
                product.views_number += 1
                product.save()
        else:
            product.views_number += 1
            product.save()


        context = {
            'product': product
        }

        return render(request, 'detail.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('choice') == "like":
            productid = request.POST.get("productid")
            product = ProductModel.objects.get(id=productid)

            if not LikeModel.objects.filter(user=request.user, product=product).exists():
                LikeModel.objects.create(user=request.user, product=product)
        
            return redirect("product:detail", productid)
        
        elif request.POST.get('choice') == "comment":
            productid = request.POST.get("productid")
            product = ProductModel.objects.get(id=productid)
            comment = request.POST.get("comment")
            CommentModel.objects.create(user=request.user, product=product, comment=comment)

            return redirect("product:detail", productid)

        


