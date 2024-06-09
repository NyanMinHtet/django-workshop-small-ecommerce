from django.contrib import admin
from . models import Product,ProductDetail,Receipt

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_filter = ("category",)
    list_display = ('name','price','category')

class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ('product','color','info')

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('cus_name','email','address','payment_method')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDetail, ProductDetailAdmin)
admin.site.register(Receipt, ReceiptAdmin)