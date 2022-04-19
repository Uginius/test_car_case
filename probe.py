from pprint import pprint
import requests

BASE = 'http://127.0.0.1:5000/'
r = requests.get(BASE + 'vehicle/car2')
result_data = r.json()
pprint(result_data)


r = requests.put(BASE + 'vehicle/car3', {'brand': 'range_rover', 'color': 'red', 'price': 60000})
result_data = r.json()
pprint(result_data)

