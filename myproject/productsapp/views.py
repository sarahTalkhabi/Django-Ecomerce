from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import product
# Create your views here.
def index(request):
    return HttpResponse('helloo')

def products(request):

    products = product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'productsapp/index.html',context)

def product_detail(request,id):
    Product = product.objects.get(id=id)
    context = {
        'product': Product
    }
    return render(request,'productsapp/detail.html',context)
@login_required
def add_product(request):
    if request.method=='POST' and 'upload' in request.FILES:
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        file = request.FILES
        image = file['upload']
        seller_name = request.user
        Product = product(name=name,price=price,desc=desc,image=image,seller_name=seller_name)
        Product.save()
    return render(request,'productsapp/add.html')
def update_product(request,id):
    Product = product.objects.get(id=id)
    if request.method == 'POST':
        Product.name = request.POST.get('name')
        Product.price = request.POST.get('price')
        Product.desc = request.POST.get('desc')
        Product.image = request.FILES['upload']
        Product.save()
        return redirect('/productsapp/products')
    context = {
        'product': Product,
    }
    return render(request,'productsapp/update.html',context)

def delete_product(request,id):
    Product = product.objects.get(id=id)
    context={
            'product':Product  
    }
    if request.method == 'POST':
        Product.delete()
        return redirect('/productsapp/products')
    return render(request,'productsapp/delete.html',context)

def my_listing(request):
    products = product.objects.filter(seller_name=request.user)
    context = {
        'products': products,
    } 

    return render(request,'productsapp/mylisting.html',context)    

def contact(request):
    products = product.objects.filter(seller_name=request.user)
    context = {
        'products': products,
    } 

    return render(request,'productsapp/contact.html',context)    