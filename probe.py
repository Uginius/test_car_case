from pprint import pprint
import requests


def show_all_cars():
    print('show all cars')
    pprint(requests.get(BASE + '0').json())


BASE = 'http://127.0.0.1:5000/vehicle/'
cars_list = BASE + 'cars'

req_put = requests.put(BASE + '5', {'brand': 'RangeRover', 'color': 'gold', 'price': '60000'})
pprint(req_put.json())
pprint(requests.get(BASE + '2').json())
show_all_cars()
# pprint(requests.post(cars_list).json())
