from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile,Products
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile
from .amazon import checkprice
from .mail import send_email
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

from apscheduler.schedulers.background import BackgroundScheduler

from .forms import UserForm,ProfileForm
# Create your views here.

@login_required
def user_logout(request):
    logout(request)
    redirect('home')



def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(priceloop, 'interval', minutes=10)
    scheduler.start()


def priceloop():
    products=Products.objects.all()
    print(products)
    if products:
        for product in products:
            detail=checkprice(product.url)
            old_price=product.price
            new_price=float(detail[1][2:].replace(',',''))
            if old_price<=new_price:
                print("grab the deal")
                send_email("Hurry! Price dropped Grab the deal","Current price of "+detail[0]+" is "+detail[1],product.user.email)


@login_required
def price(request):
    if request.method == "POST":
        url = request.POST.get('url')
        print(url)
        detail=checkprice(url)
        title = detail[0]
        price=float(detail[1][2:].replace(',', ''))
        print(price)
        form=Products(user=request.user,title=title,price=price,url=url)
        form.save()
        print("product detail saved successfully!")
        send_email("Price Hawk","Current price of "+detail[0]+" is "+detail[1],request.user.email)


    return render(request,'price/price.html')

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

        if form.is_valid() :
            user=form.save(commit=False)
            email=form.cleaned_data.get('email')
            user.username=email
            user.save()
            profile=Profile(user=user,mobile=request.POST.get('mobile'))
            # profile=profileform.save(commit=False)
            # profile.user=user
            profile.save()
            messages.success(request,"Your account has been created!")
            print("account created")
            send_email("Congratulations! Account created at PriceHawk","Click on this link to get notifications directon whatsapp == \n https://wa.me/14155238886?text=join%20note-outer",email)
            return redirect('home')
        else:
            messages.warning(request,'Passwords do not Matched!')

    else:
        form=UserForm()

    return render(request,"price/signup.html",{'form':form})
