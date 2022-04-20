import requests
from flask import request


def form_get(el):
    return request.form.get(el)


class Car:
    def __init__(self, car_id, brand=None, color=None, price=None):
        self.car_id = car_id
        self.brand = brand
        self.color = color
        self.price = price
        self.url = f'http://127.0.0.1:5000/vehicle/{car_id}'

    def properties(self):
        return {'brand': self.brand, 'color': self.color, 'price': self.price}

    def add_car_to_dealer(self):
        print(f'adding car #{self.car_id}')
        requests.put(self.url, self.properties())

    def show_car(self):
        print(f'looking for car #{self.car_id} in dealer office')
        return requests.get(self.url).json()
