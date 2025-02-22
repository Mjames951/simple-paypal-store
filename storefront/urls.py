from django.urls import path
from . import views

urlpatterns = [
    path('create/order/<itemid>/', views.createOrderRemote, name='createorder'),
    path('capture/order/<itemid>/', views.captureOrder, name='captureorder'),


    path('', views.store, name="store"),
    path('item/<itemname>/', views.itemPage, name='itempage'),
    path('checkout/<itemid>/', views.checkout, name="checkout"),
    path('checkout/success/<itemid>/', views.paymentSuccessful, name="paymentsuccessful"),
    path('checkout/fail/<itemid>/', views.paymentFailed, name="paymentfailed"),
]