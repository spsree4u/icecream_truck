from django.db import models

# Create your models here.


class Truck(models.Model):

    class Meta:
        db_table = "truck"


class Item(models.Model):

    name = models.CharField(max_length=256)
    flavour = models.CharField(max_length=256, null=True)
    price = models.FloatField()

    class Meta:
        db_table = "item"

    def __str__(self):
        return f"{self.name}_{self.flavour}" if self.flavour else self.name


class Inventory(models.Model):

    item = models.ForeignKey(Item, related_name="inventory_item",
                             on_delete=models.CASCADE)
    truck = models.ForeignKey(Truck, related_name="inventory_truck",
                              on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    income = models.FloatField(default=0)

    class Meta:
        db_table = "inventory"
