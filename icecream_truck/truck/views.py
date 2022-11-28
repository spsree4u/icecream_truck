from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Sum

from truck.models import Truck, Item, Inventory
from truck.serializers import TruckSerializer, ItemSerializer, \
    InventorySerializer

# Create your views here.


class TruckViewSet(viewsets.ModelViewSet):
    serializer_class = TruckSerializer

    def get_queryset(self):
        truck = Truck.objects.all()
        return truck


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        category = Item.objects.all()
        return category


class InventoryViewSet(viewsets.ModelViewSet):
    serializer_class = InventorySerializer

    def get_queryset(self):
        part_model = Inventory.objects.all()
        return part_model


@api_view(['POST'])
def buy_item(request, format=None):

    if request.method == 'POST':
        item_name = request.data.get('item')
        flavour = request.data.get('flavour')
        truck_id = request.data.get('truck_id')
        item = Item.objects.get(name=item_name, flavour=flavour)
        item_id = item.id
        item_price = item.price
        # truck_id = Truck.objects.get(id=truck_id)
        quantity = request.data.get('quantity')
        inventory = Inventory.objects.get(item_id=item_id, truck_id=truck_id)
        if inventory.quantity >= quantity:
            inventory.quantity -= quantity
            inventory.income += (quantity * item_price)
            inventory.save()
            return Response("ENJOY!", status.HTTP_202_ACCEPTED)
        else:
            return Response("SORRY!", status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def inventory(request, format=None):
    truck_id = request.query_params.get('truck_id')
    try:
        inventory_details = Inventory.objects.filter(truck_id=truck_id)
        total_income = Inventory.objects.aggregate(
            Sum('income'))['income__sum']
    except Inventory.DoesNotExist:
        return Response("Inventory data not found", status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        inventory_serializer = InventorySerializer(inventory_details,
                                                   many=True)
        if inventory_serializer.is_valid:
            truck_details = {"total_price": total_income,
                             "inventory": inventory_serializer.data}
            return Response(truck_details, status.HTTP_200_OK)

    return Response("Error finding inventory", status.HTTP_404_NOT_FOUND)
