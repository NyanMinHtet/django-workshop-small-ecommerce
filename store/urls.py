from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name = "home"),
    path("product_detail",views.product_detail, name="pd_detail"),
    path("checkout",views.checkout, name="checkout")
]