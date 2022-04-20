from flask_restful import Resource, reqparse


# put_car_args = reqparse.RequestParser()
# put_car_args.add_argument('brand', type=str, help='car brand', required=True)
# put_car_args.add_argument('color', type=str, help='car color', required=True)
# put_car_args.add_argument('price', type=int, help='car price', required=True)

# args = put_car_args.parse_args()

class Vehicle(Resource):
    def __init__(self):
        self.cars = {1: {'brand': 'chevrolet', 'color': 'black', 'price': 5000},
                     2: {'brand': 'geely', 'color': 'gray', 'price': 12000},
                     3: {'brand': 'kia', 'color': 'red', 'price': 10000}}

    def get(self):
        # return self.cars if car_id == 'cars' else self.cars[car_id]
        return {'data': self.cars}

    def post(self):
        # return self.cars if car_id == 'cars' else self.cars[car_id]
        return {'data': 'posted'}
