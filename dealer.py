from pprint import pprint

from flask import request
from flask_restful import Resource

from vehicle import Car

cars = {}


def form_get(el):
    return request.form.get(el)


class Dealer(Resource):

    def get(self, car_id):
        if car_id == 0:
            return {'cars': cars}
        try_dict = cars.get(car_id)
        if not try_dict:
            return {car_id: "The dealer don't have this car"}
        return {car_id: try_dict}

    def put(self, car_id):
        car = Car(car_id, brand=form_get('brand'), color=form_get('color'), price=form_get('price'))
        cars[car_id] = car.properties()
        return {car_id: cars[car_id]}, 201
