from rest_framework import serializers

from truck.models import Truck, Item, Inventory


class TruckSerializer(serializers.ModelSerializer):

    class Meta:
        model = Truck
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = '__all__'
