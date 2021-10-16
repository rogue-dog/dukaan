

from django.db.models import fields
from rest_framework import serializers

from .models import Item


class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['price', 'item_name', 'image_url', 'pk']
