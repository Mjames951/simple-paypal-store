from django.shortcuts import render, get_object_or_404, redirect
from .models import Item

def store(request, message=None):
    items = Item.objects.filter(sold=False)
    return render(request, "storefront/store.html", {
        "items": items,
        "message": message,
    })

def itemPage(request, itemname):
    try: item = get_object_or_404(Item, name=itemname)
    except: return store(request, message="Sorry, item doesn't exist.")
    return render(request, "storefront/itempage.html", {
        "item": item,
    })

def checkout(request, itemid):
    try: item = get_object_or_404(Item, id=itemid)
    except: return redirect('store', message="Sorry, item doesn't exist or has been sold.")
    return render(request, "storefront/checkout.html", {
        "item": item,
    })