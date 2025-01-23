from django.shortcuts import render, get_object_or_404, redirect
from .models import Item

def store(request, message=None):
    items = Item.objects.all()
    return render(request, "storefront/store.html", {
        "items": items,
        "message": message,
    })

def checkout(request, itemid):
    try: get_object_or_404(Item, id=itemid)
    except: return redirect('store', message="Sorry, item doesn't exist or has been sold.")
    return render(request, "storefront/checkout.html", {
        
    })