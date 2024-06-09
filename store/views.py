from django.shortcuts import render
from .models import Product, ProductDetail, Receipt
from .forms import ReceiptForm

# Create your views here.
def home_page(request,slug = None):
    if slug != None:
        products = Product.objects.filter(category = slug)
    else:
        products = Product.objects.all()
    return render(request, "index.html", 
                  {'feature': products, 'recent': range(5)},
                )

def product_detail(request,pd_id,color=None):
    pd_detail = ProductDetail.objects.filter(product=pd_id)
    product = Product.objects.get(pk=pd_id)
    if id != None:
        selfinfo = ProductDetail.objects.filter(product = pd_id, color = color)
        if selfinfo:
            selfinfo = selfinfo[0]
        else:
            selfinfo = False
    else:
        selfinfo = False
    return render(request, "product_detail.html",{
        'info':pd_detail,
        'product':product,
        'selfinfo':selfinfo,
    })

def checkout(request,pd_id,color):
    if request.method == "POST":
        selfinfo = ProductDetail.objects.filter(product = pd_id, color = color)
        if selfinfo:
            form = ReceiptForm(request.POST)
            if form.is_valid():
                recipt = form.save(commit = False)
                recipt.productdetail = selfinfo[0]
                recipt.save()
    
    return render(request, "checkout.html",
                  {
                      "form": ReceiptForm
                  })