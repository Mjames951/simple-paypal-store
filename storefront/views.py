from django.shortcuts import render

def store(request):
    return render(request, "storefront/store.html", {

    })

def checkout(request):
    return render(request, "storefront/checkout.html", {
        
    })