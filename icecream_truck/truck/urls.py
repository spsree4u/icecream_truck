from django.urls import path, include
from rest_framework.routers import DefaultRouter

from truck.views import TruckViewSet, ItemViewSet, InventoryViewSet, \
    buy_item, inventory

router = DefaultRouter()
router.register("trucks", TruckViewSet, basename="trucks")
router.register("items", ItemViewSet, basename="items")
router.register("inventory", InventoryViewSet, basename="inventory")

urlpatterns = [
    path('', include(router.urls)),
    path('buy/', buy_item, name='buy'),
    path('inventory', inventory, name='inventory')
]
