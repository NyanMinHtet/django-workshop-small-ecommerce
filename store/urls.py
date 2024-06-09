from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name = "home"),
    path("product_detail/<int:pd_id>",views.product_detail, name="pd_detail"),
    path("checkout/<int:pd_id>/<str:color>",views.checkout, name="checkout"),
    path("categroy/<slug:slug>", views.home_page, name = "cat"),
    path("product_detail/<int:pd_id>/<str:color>",views.product_detail, name="pd_detail_color"),
]