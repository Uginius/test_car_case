# 1. Создать небольшое REST API на Python (можно использовать любые библиотеки и framework-и, в т.ч. Flask).

# 2. Требуется создание только бэкэнд части, в readme файле желательно описать endpoint и примеры запросов
# (будет плюсом наличие файлов-схем запросов, например JSON Schema).

# 3. Данное API должно поддерживать CRUD операции.

# 4. Тематика данного API связана с продажами машин автодилерами.
# Модель данных (в т.ч. описание и взаимодействие между классами "Машина" и "Дилер") можете разработать любую,
# на ваше усмотрение, но соответствующую условиям выше.


from flask import Flask, request
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

put_car_args = reqparse.RequestParser()
put_car_args.add_argument('brand', type=str, help='car brand')
put_car_args.add_argument('color', type=str, help='car color')
put_car_args.add_argument('price', type=int, help='car price')


class Vehicle(Resource):
    def __init__(self):
        self.cars = {'car1': {'brand': 'chevrolet', 'color': 'black', 'price': 5000},
                     'car2': {'brand': 'geely', 'color': 'gray', 'price': 12000},
                     'car3': {'brand': 'kia', 'color': 'red', 'price': 10000}}

    def get(self, name):
        return self.cars if name == 'cars' else self.cars[name]

    def put(self, name):
        rf = request.form['brand']
        print(rf)
        return self.cars[name]


api.add_resource(Vehicle, '/vehicle/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
