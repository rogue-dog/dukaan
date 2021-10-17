from datetime import datetime
from django.db import models
from django.db.models.expressions import Value
from django.core.validators import validate_comma_separated_integer_list
from django.db.models.query_utils import DeferredAttribute

# Create your models here.


class User(models.Model):
    email = models.CharField(max_length=250, primary_key=True)
    password = models.CharField(max_length=250)
    name = models.CharField(max_length=100)


class Item (models.Model):
    item_name = models.CharField(max_length=250)

    price = models.IntegerField()
    image_url = models.CharField(max_length=250)


class Cart(models.Model):
    user_id = models.CharField(max_length=250, primary_key=True)
    items = models.JSONField(default=dict)
    total = models.IntegerField()


class UserVerification(models.Model):
    email = models.CharField(max_length=250, primary_key=True)
    otp = models.CharField(max_length=4)


class Order(models.Model):
    items = models.JSONField()

    total = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True)

    user_id = models.CharField(max_length=250)
