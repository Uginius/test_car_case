from pprint import pprint

from flask import request
from flask_restful import Resource

cars = {1: {'brand': 'chevrolet', 'color': 'black', 'price': 5000},
        2: {'brand': 'ford', 'color': 'gray', 'price': 12000},
        3: {'brand': 'kia', 'color': 'red', 'price': 10000}}


class Dealer(Resource):

    def get(self, car_id):
        if car_id == 0:
            return {'cars': cars}
        try_dict = cars.get(car_id)
        if not try_dict:
            return {car_id: "The dealer don't have this car"}
        return {car_id: try_dict}

    def put(self, car_id):
        new_car = {'brand': request.form['brand'],
                   'color': request.form['color'],
                   'price': request.form['price'],
                   }
        cars[car_id] = new_car
        return {car_id: new_car}
