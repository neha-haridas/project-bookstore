from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Category

# Create your views here.
def index(request):
    tblBook = Book.objects.all()
    category = Category.objects.all()
    return render(request,'index.html',{'datas':tblBook,'category':category})
# def category(request):
#     tblcategory = Category.objects.all()
#     return render(request,'index.html',{'datas':tblcategory})

def product(request):
    tblBooks = Book.objects.all()
    return render(request, 'product.html', {'datass': tblBooks})
def checkout(request):
    return render(request,'checkout.html')