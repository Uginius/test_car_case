from flask import request
from flask_restful import Resource


# put_car_args = reqparse.RequestParser()
# put_car_args.add_argument('brand', type=str, help='car brand', required=True)
# put_car_args.add_argument('color', type=str, help='car color', required=True)
# put_car_args.add_argument('price', type=int, help='car price', required=True)

# args = put_car_args.parse_args()

class Vehicle(Resource):
    def __init__(self):
        self.cars = {1: {'brand': 'chevrolet', 'color': 'black', 'price': 5000},
                     2: {'brand': 'ford', 'color': 'gray', 'price': 12000},
                     3: {'brand': 'kia', 'color': 'red', 'price': 10000}}

    def get(self, car_id):
        # return {'cars': self.cars} if name == 'cars' else {name: self.cars[name]}
        return {car_id: self.cars[car_id]}

    def put(self, car_id):
        new_car = {'brand': request.form['brand'],
                   'color': request.form['color'],
                   'price': request.form['price'],
                   }
        self.cars[car_id] = new_car
        return {car_id: new_car}
