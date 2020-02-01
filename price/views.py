from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile
from .amazon import checkprice
from .mail import send_email
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

from .forms import UserForm
# Create your views here.

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

def price(request):
    if request.method == "POST":
        email = request.POST.get('email')
        url = request.POST.get('url')
        print(url)
        check=Profile.objects.filter(email=email).exists()
        # if not check:
        #     form = Profile(email=email)
        #     form.save()
        #     prod = Products(user=form,url=url)
        #     prod.save()
        price = checkprice(url)
        send_email(price,email)


    return render(request,'price/index.html')

def home(request):
    return render(request,"price/base.html")

def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        user=authenticate(username=email,password=password)
        if user:
            login(request,user)
            messages.success(request,"You have been logged in!")
            print("logged in")
            return redirect('home')
        else:
            messages.warning(request,'Wrong input!')
    return render(request,"price/login.html")


def register(request):
    if request.method == "POST":
        form=UserForm(data=request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=form.cleaned_data.get('email')
            user.save()
            profile=Profile(user=user)
            profile.save()
            messages.success(request,"Your account has been created!")
            print("account created")
            return redirect('home')
        else:
            messages.warning(request,'Passwords do not Matched!')

    else:
        form=UserForm()
    return render(request,"price/signup.html",{'form':form})
