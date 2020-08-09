from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
import create_tables
from resources.item import Item, GetSingleItem

app = Flask(__name__)
app.secret_key = 'test'
api = Api(app)

jwt = JWT(app, authenticate, identity)

create_tables.maketable()
api.add_resource(Item, '/item')
api.add_resource(GetSingleItem, '/item/<string:itemname>')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    app.run(port=5000, debug=True)