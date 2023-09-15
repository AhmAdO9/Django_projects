from django.shortcuts import render
from .models import Product,Order
from math import ceil
from django.http import HttpResponse
import json

def home(request):
     products = Product.objects.values("category", "id")
     allProds = []
     cats = {item["category"][0:1].upper()+item["category"][1:] for item in products}
     for cat in cats:
          prods = Product.objects.filter(category=cat)
          nSlides = ceil(len(prods)/4)  
          allProds.append([prods, range(len(prods)), range(nSlides)])

     params = {"allProds":allProds}
     return render(request, "shop/home.html", params) 
def about(request):
    return render(request, "shop/about.html") 
def contact(request):
     return render(request, "shop/contact.html") 
def tracker(request):
     if request.method == "POST":
          Email = request.POST.get("Email",'')
          orderId = request.POST.get("orderId",'')
          print(Email)
      
          try:
               order = Order.objects.filter(email = Email, orderId= orderId)
               updates=[]
               for item in order:
                    updates.append({"text":"Thank you for ordering from us!","time":item.timestamp})
               response = json.dumps(updates, default = str) 
               return HttpResponse(response)
          except Exception as e:
               print(e)
               return render(request, "shop/tracker.html") 
        
     return render(request, "shop/tracker.html") 
   
def search(request):
     return render(request, "shop/search.html") 
def productview(request, id):
     prod = Product.objects.get(id=id)
 
     return render(request, "shop/prodview.html",{
     'prod':prod})
def checkout(request):
     try:
          email = request.POST.get('emaily')
          object = Order(email = email)
          object.save()
          return render(request, "shop/checkout.html")
     except:
          return render(request, "shop/checkout.html")

def checkoutData(request):

     return render(request, "shop/checkout.html") 
