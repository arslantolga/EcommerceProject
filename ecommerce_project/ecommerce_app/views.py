from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.urls import reverse


# Create your views here.

def mainpage(request):
    return render(request, "ecommerce_app/mainpage.html")

def login(request):
    return render(request, "ecommerce_app/login.html")

def signup(request):
    if request.POST:
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        address = request.POST["address"]
        city = request.POST["city"]
        state = request.POST["state"]
        models.buyer.objects.create(name=name, email=email, password=password, address=address, city=city, state=state)
        return redirect(reverse("ecommerce_app:storepage"))
    return render(request, "ecommerce_app/signup.html")

def storepage(request):
    all_user = models.buyer.objects.all()
    user_dic = {"user":all_user}
    return render(request, "ecommerce_app/storepage.html", context=user_dic)