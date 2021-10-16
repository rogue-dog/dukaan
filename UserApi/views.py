from django.http import response
from django.shortcuts import render
import rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, serializers
from UserApi.models import Cart, Item, Order, User, UserVerification
from UserApi.send_otp import send_otp
from UserApi.serializers import ItemSerializers

# Create your views here.


@api_view(['GET'])
def login(request):
    email = request.headers['email']
    password = request.headers['password']
    body = {"": ""}
    if(User.objects.filter(email=email, password=password).exists()):
        message = "Welcome"
        success = True
        user = User.objects.get(email=email)
        body = {
            "email": getattr(user, "email"),
            "name": getattr(user, "name")
        }
    else:
        message = "Incorrect Credentials"
        success = False

    return(Response({"message": message, "success": success, "body": body}))


@api_view(['POST'])
def SignUp(request):
    name = request.data['name']
    email = request.data['email']
    password = request.data['password']
    new_user = User(email=email, password=password, name=name)
    new_user.save()
    return (Response({"success": True}))


@api_view(['POST'])
def add_item(req):
    price = req.data['price']
    item_name = req.data['item_name']
    image_url = req.data['image_url']
    new_item = Item(price=price, item_name=item_name, image_url=image_url)
    new_item.save()
    return(Response({"success": True}))


class GetItem(generics.ListAPIView):
    # model = Item
    serializer_class = ItemSerializers
    queryset = Item.objects.all()


@api_view(['GET'])
def EmailVerification(req):
    email = req.headers['email']
    success, message = send_otp(email)
    return(Response({"success": success, "message": message}))


@api_view(['GET'])
def OTPCheck(req):
    email = req.headers['email']
    otp = req.headers['otp']
    if(UserVerification.objects.filter(email=email, otp=otp).exists()):
        UserVerification.objects.filter(email=email).delete()
        return(Response({"success": True, "message": "Welcome!!"}))
    else:
        return(Response({"success": False, "message": "Incorrect OTP"}))


@api_view(['POST'])
def add_cart(req):
    user_id = req.data['user_id']
    items = req.data['items']
    total = req.data['total']
    Cart(user_id=user_id, items=items, total=total).save()
    return (Response({"success": True}))


@api_view(['GET'])
def get_cart(req):
    user_id = req.headers['userId']
    if(Cart.objects.filter(user_id=user_id).exists()):
        cart = Cart.objects.get(user_id=user_id)
        return(Response({"success": True, "items": getattr(cart, "items"), "total": getattr(cart, "total")}))
    return(Response({"success": False, "message": "No Existing Cart Found, Please Add something to Cart"}))


@api_view(['POST'])
def place_order(req):
    user_id = req.data['user_id']
    items = req.data['items']
    total = req.data['total']
    order = Order(user_id=user_id, items=items, total=total)
    order.save(force_insert=True)
    Cart.objects.filter(user_id=user_id).delete()
    return (Response({"success": True, "datetime": order.datetime}))


@api_view(['GET'])
def get_order(req):
    user_id = req.headers['userId']
    if(Order.objects.filter(user_id=user_id).exists()):
        quer = Order.objects.filter(user_id=user_id).order_by("datetime")
        success = True
        orders = []
        for order in quer:
            details = {
                "items": getattr(order, "items"),
                "datetime": getattr(order, "datetime"),
                "total": getattr(order, "total")
            }
            orders.append(details)
        return (Response({"success": True, "details": orders}))
    return(Response({"success": False}))
