from pprint import pprint
import requests

BASE = 'http://127.0.0.1:5000/'
cars_list = BASE + 'cars/cars'
car1 = BASE + 'cars/1'


pprint(requests.get(car1).json())
# pprint(requests.post(cars_list).json())
