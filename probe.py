from pprint import pprint
import requests

BASE = 'http://127.0.0.1:5000/'
cars_list = BASE + 'cars'


pprint(requests.get(cars_list).json())
pprint(requests.post(cars_list).json())
