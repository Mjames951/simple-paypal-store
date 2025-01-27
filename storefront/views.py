from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
import requests
import json
import base64

clientID = config("PAYPAL_CLIENT_ID")
clientSecret = config("PAYPAL_SECRET_KEY")

def PaypalToken(client_ID, client_Secret):

    url = "https://api.sandbox.paypal.com/v1/oauth2/token"
    data = {
        "client_id":client_ID,
        "client_secret":client_Secret,
        "grant_type":"client_credentials"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic {0}".format(base64.b64encode((client_ID + ":" + client_Secret).encode()).decode())
    }

    token = requests.post(url, data, headers=headers)
    return token.json()['access_token']



def createOrderRemote(request, itemid):
    try: item = get_object_or_404(Item, id=itemid)
    except: return redirect('store')

    token = PaypalToken(clientID, clientSecret)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+token,
    }
    json_data = {
        "intent": "CAPTURE",
        "payment_source": {
            "paypal": {
            "experience_context": {
                "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED",
                "landing_page": "LOGIN",
                "shipping_preference": "NO_SHIPPING",
                "user_action": "PAY_NOW",
                "return_url": "http://BRUH.NET:8000",
                "cancel_url": "http://BRUH.NET:8000"
            }
            }
        },
        "purchase_units": [
            {
            "invoice_id": "90210",
            "amount": {
                "currency_code": "USD",
                "value": f"{item.price}",
                "breakdown": {
                "item_total": {
                    "currency_code": "USD",
                    "value": f"{item.price}"
                }
                }
            },
            "items": [
                {
                "name": item.name,
                "description": f"{item.description}",
                "unit_amount": {
                    "currency_code": "USD",
                    "value": f"{item.price}"
                },
                "quantity": "1",
                "sku": "sku01",
                "url": "http://BRUH.NET:8000",
                "upc": {
                    "type": "UPC-A",
                    "code": "123456789012"
                }
                }
            ]
            }
        ]
    }
    
    print(item.image.url)


    response = requests.post('https://api-m.sandbox.paypal.com/v2/checkout/orders', headers=headers, json=json_data)
    print(response.json())
    #linkForPayment = response.json()['links']['href']
    #print(linkForPayment)
    return response.json()['links'][1]['href']


    #capture order aims to check whether the user has authorized payments.
def captureOrder(self, request):
    token = request.data.get('token')#the access token we used above for creating an order, or call the function for generating the token
    captureurl = request.data.get('url')#captureurl = 'https://api.sandbox.paypal.com/v2/checkout/orders/6KF61042TG097104C/capture'#see transaction status
    headers = {"Content-Type": "application/json", "Authorization": "Bearer "+token}
    response = requests.post(captureurl, headers=headers)
    return Response(response.json())





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

    link=createOrderRemote(request, itemid)

    return render(request, "storefront/checkout.html", {
        "item": item,
        "link": link,
    })

def paymentSuccessful(request, itemid):
    pass

def paymentFailed(request, itemid):
    pass