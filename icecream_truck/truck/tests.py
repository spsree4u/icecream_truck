import pytest
import requests

# Create your tests here.

HOST = "http://127.0.0.1:8300"


def test_trucks():
    trucks = requests.get(f"{HOST}/ice_cream_truck/trucks/")
    print(trucks)
    assert trucks.status_code == 200


def test_items():
    items = requests.get(f"{HOST}/ice_cream_truck/items/")
    print(items)
    assert items.status_code == 200


def test_inventory():
    inventory = requests.get(f"{HOST}/ice_cream_truck/inventory/")
    print(inventory)
    assert inventory.status_code == 200


def test_buy():
    """This test will work until the table has data as we are testing
    real db here. This is just for testing purpose of API"""
    data = {
        "item": "Ice cream",
        "flavour": "Chocolate",
        "truck_id": 1,
        "quantity": 5
    }
    buy = requests.post(f"{HOST}/ice_cream_truck/buy/", json=data)
    print(buy)
    assert buy.status_code == 202
    assert buy.content.decode("utf-8") == '"ENJOY!"'


def test_buy_fail():
    data = {
        "item": "Shaved Ice",
        "flavour": None,
        "truck_id": 1,
        "quantity": 555
    }
    buy = requests.post(f"{HOST}/ice_cream_truck/buy/", json=data)
    print(buy)
    assert buy.status_code == 404
    assert buy.content.decode("utf-8") == '"SORRY!"'


def test_truck_inventory():
    trucks = requests.get(f"{HOST}/ice_cream_truck/inventory?truck_id=1")
    print(trucks)
    assert trucks.status_code == 200
