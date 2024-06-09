from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, "index.html", {'feature': range(9), 'recent': range(5)})

def product_detail(request):
    return render(request, "product_detail.html")

def checkout(request):
    return render(request, "checkout.html")