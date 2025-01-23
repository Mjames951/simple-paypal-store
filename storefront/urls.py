from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('checkout/<itemid>/', views.checkout, name="checkout"),
]