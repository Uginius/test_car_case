from flask import Flask
from flask_restful import Api
from vehicle import Vehicle

# 1. Создать небольшое REST API на Python (можно использовать любые библиотеки и framework-и, в т.ч. Flask).

# 2. Требуется создание только бэкэнд части, в readme файле желательно описать endpoint и примеры запросов
# (будет плюсом наличие файлов-схем запросов, например JSON Schema).

# 3. Данное API должно поддерживать CRUD операции.

# 4. Тематика данного API связана с продажами машин автодилерами.
# Модель данных (в т.ч. описание и взаимодействие между классами "Машина" и "Дилер") можете разработать любую,
# на ваше усмотрение, но соответствующую условиям выше.

app = Flask(__name__)
api = Api(app)
api.add_resource(Vehicle, '/vehicle/<int:car_id>')

if __name__ == '__main__':
    app.run(debug=True)
