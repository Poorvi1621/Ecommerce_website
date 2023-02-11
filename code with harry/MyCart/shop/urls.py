
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="shopIndex"),
     path("about/",views.about, name="aboutus"),
    path("contact/",views.contact, name="contactus"),
    path("tracker/",views.tracker, name="trackyourorder"),
    path("search/",views.search, name="search"),
    path("products/<int:myId>",views.productView, name="productView"),
    path("checkout/",views.checkout, name="checkout"),     
]
