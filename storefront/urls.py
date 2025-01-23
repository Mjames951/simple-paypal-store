from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('item/<itemname>/', views.itemPage, name='itempage'),
    path('checkout/<itemid>/', views.checkout, name="checkout"),
]