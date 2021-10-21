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
    return (Response({"success": True, "message": "Account Created!"}))


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
