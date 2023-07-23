from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Product


# Create your views here.

def Home(Request):
    products = Product.objects.all().order_by('id')
    return render(Request, "Home.html", {"products": products})


def AddProduct(Request):
    return render(Request, "AddProduct.html")


def UploadProduct(Request):
    p = Product()
    p.name = Request.POST.get('name')
    p.price = Request.POST.get('price')
    p.weight = Request.POST.get('weight')
    p.deliveryCharges = Request.POST.get('charges')
    p.expiryDate = Request.POST.get('expiry')
    p.imgPath = Request.POST.get('imgPath')

    p.save()
    return redirect("/")


def EditProduct(Request, id):
    product = Product.objects.get(id=id)
    return render(Request, "editProduct.html", {'product': product})


def UpdateProduct(Request, id):
    p = Product.objects.get(id=id)
    p.name = Request.POST.get('name')
    p.price = Request.POST.get('price')
    p.weight = Request.POST.get('weight')
    p.deliveryCharges = Request.POST.get('charges')
    p.imgPath = Request.POST.get('imgPath')

    p.save()
    messages.success(Request, f'Product "{p.name}" Edited Successfully!')
    return redirect("/")


def DeleteProduct(Request, id):
    p = Product.objects.get(id=id)
    p.delete()
    messages.success(Request, f'Product "{p.name}" Deleted Successfully!')
    return redirect("/")
