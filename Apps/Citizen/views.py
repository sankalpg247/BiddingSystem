from django.shortcuts import render, redirect

from .models import Order
from ..Farmer.models import Product


# Create your views here.

def buy(Request, id):
    product = Product.objects.get(id=id)
    return render(Request, "buyNow.html", {"product": product})


def placeOrder(Request):
    o = Order()
    o.citizenName = Request.POST.get("username")
    o.productName = Request.POST.get("name")
    o.qty = 1
    o.amountPaid = Request.POST.get("total")
    o.contact = Request.POST.get("contact")
    o.address = Request.POST.get("address")
    o.save()
    return redirect("/")
