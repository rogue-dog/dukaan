"""ProjectX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from UserApi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', views.SignUp),
    path('login', views.login),
    path('item/post', views.add_item),
    path('item/get', views.GetItem.as_view()),
    path('check/email', views.EmailVerification),
    path('check/otp', views.OTPCheck),
    path('add/cart', views.add_cart),
    path('get/cart', views.get_cart),
    path('order/place', views.place_order),
    path('order/get', views.get_order),

]
