from pprint import pprint
import requests
from vehicle import Car

BASE = 'http://127.0.0.1:5000/vehicle/'


def show_all_cars():
    print('show all cars')
    pprint(requests.get('http://127.0.0.1:5000/vehicle/0').json())


cars = [Car(car_id=1, brand='Chevrolet', color='black', price='25000'),
        Car(car_id=2, brand='Ford', color='gray', price='22000'),
        Car(car_id=3, brand='Audi', color='blue', price='55000'),
        Car(car_id=4, brand='BMW', color='cyan', price='88000'),
        Car(car_id=5, brand='Mazda', color='green', price='54000'),
        Car(car_id=6, brand='Opel', color='yellow', price='37000'),
        Car(car_id=7, brand='Kia', color='red', price='24000')]

for car in cars:
    car.add_car_to_dealer()

car99 = Car(car_id=99, brand='Tesla')
car99.add_car_to_dealer()

show_all_cars()

car_id_to_delete = 1
pprint(requests.delete(f'{BASE}{car_id_to_delete}').json())

car_to_modify = 3
pprint(requests.put(f'{BASE}{car_to_modify}', {'price': 61000}).json())

show_all_cars()
