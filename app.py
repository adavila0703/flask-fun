from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from user import UserRegister
import create_tables
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'test'
api = Api(app)

jwt = JWT(app, authenticate, identity)

create_tables.maketable()
api.add_resource(Item, '/item')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    app.run(port=5000, debug=True)