from pprint import pprint
import requests

from vehicle import Car


def show_all_cars():
    print('show all cars')
    pprint(requests.get(BASE + '0').json())


cars = [Car(car_id=1, brand='Chevrolet', color='black', price='25000'),
        Car(car_id=2, brand='Ford', color='gray', price='22000'),
        Car(car_id=3, brand='Audi', color='blue', price='55000'),
        Car(car_id=4, brand='BMW', color='cyan', price='88000'),
        Car(car_id=5, brand='Mazda', color='green', price='54000'),
        Car(car_id=6, brand='Opel', color='yellow', price='37000'),
        Car(car_id=7, brand='Kia', color='red', price='24000')]

for car in cars:
    car.add_car_to_dealer()
    # print(car.show_car())

BASE = 'http://127.0.0.1:5000/vehicle/'
cars_list = BASE + 'cars'

# req_put = requests.put(BASE + '5', {'brand': 'RangeRover', 'color': 'gold', 'price': '60000'})
# pprint(req_put.json())
# pprint(requests.get(BASE + '2').json())
show_all_cars()
# pprint(requests.post(cars_list).json())
