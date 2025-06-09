from django.shortcuts import render,redirect,reverse
from django.views import View
from .admin import LoginForm , OtploginForm , CheckOtpForm
from django.contrib.auth import authenticate, login ,logout
from random import randint
from account.models import Otp,User
import ghasedakpack
from django.utils.crypto import get_random_string
from uuid import uuid4


SMS = ghasedakpack.Ghasedak("b4f8d77dfd2aaea9275d9a113c4825e0452893ae36ed3333797dea152c32d805LSZeryMyLPnu2SQ5")



# Create your views here.


# def user_login(request):
#     return render(request,'account/login.html')

class UserLogin(View):
    def get(self , request):
        form = LoginForm()
        return render(request , "account/login.html",{'form':form})

    def post(self , request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                form.add_error('phone','invalid user data')

        else:
            form.add_error('phone','invalid data')  

        return render(request , 'account/login.html',{'form':form})
              
class OtpLoginView(View):
     def get(self , request):
        form = OtploginForm()
        return render(request , "account/otplogin.html",{'form':form})   
   
     def post(self , request):
        form = OtploginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(1000,9999) 
            SMS.verification({'receptor':cd["phone"],'type':'1','template':'Ghasedak','param1':randcode})
            token = str(uuid4)
            Otp.objects.create(phone=cd['phone'],code=randcode,token=token)
            print(randcode)
            return redirect(reverse('account:check_otp')+ f'?token={token}')
        else:
            form.add_error('phone','invalid data')  

        return render(request , 'account/otplogin.html',{'form':form})
     
class CheckOtpView(View):
    def get(self , request):
        form = CheckOtpForm()
        return render(request , "account/check_otp.html",{'form':form})   
   
    def post(self , request):
        token = request.GET.get('token')
        form = CheckOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['code'],token=token).exists():
                otp= Otp.objects.get(token=token)
                user, is_created = User.objects.get_or_create(phone=otp.phone)
                user.backend = "django.contrib.auth.backends.ModelBackend"
                login(request,user)
                otp.delete()
                return redirect('/')
        else:
            form.add_error('phone','invalid data')  
        return render(request , 'account/check_otp.html',{'form':form})
    
def user_logout(request):
    logout(request)
    return redirect('/')
    