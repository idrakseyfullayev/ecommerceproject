from django.shortcuts import render, redirect , HttpResponse
from django.views import generic
import re
from account.models import Account
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def check_password(password_):
    if (len(password_) > 5 and re.search('[0-9]', password_) and 
        (re.search('[a-z]', password_) or re.search('[A-z]', password_))):
        return True
    else:
        return False



class RegisterView(generic.View):
    def get(self, request, *args, **kwargs):

        return render(request, 'register.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username:
            messages.info(request, "İstifadəçi adını daxil edin")

        if not password:
            messages.info(request, "Zəhmət olmasa parol daxil edin")    


        if username and password:
            if Account.objects.filter(username=username):
                messages.info(request, 'Lütfən, başqa istifadəçi adı daxil edin')
            elif not check_password(password):
                messages.info(request, "Şifrə hərf və rəqəmlərdən ibarət olmalıdır, minimum uzunluq 6 simvoldan ibarət olmalıdır")       
            else:
                Account.objects.create_user(username=username, password=password)
                messages.success(request, 'İstifadəçi yaradıldı')
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('product:index')



        return redirect('account:register')
    
    
class LoginView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("product:index")
        else:
            messages.info(request, "İstifadəçi tapılmadı")
            return redirect('account:login')    


class LogoutView(generic.View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('product:index')
    

