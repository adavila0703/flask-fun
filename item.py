from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


class ItemStorage(Resource):
    def __init__(self, itemname, stock, price):
        self.itemname = itemname
        self.stock = stock
        self.price = price

    def find_item_name(self, itemname):
        connection = sqlite3.connect('userdata.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items WHERE itemname=?'

        result = cursor.execute(query, (itemname,))

        row = result.fetchone()

        if row:
            item = row
        else:
            item = None
        return item


class Item(Resource):
    #@jwt_required()
    def get(self, name):
        connect

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('itemname',
                            type=str,
                            required=True,
                            help='This field cannot be blank!'
                            )
        parser.add_argument('stock',
                            type=int,
                            required=True,
                            help='This field cannot be blank!'
                            )
        parser.add_argument('price',
                            type=int,
                            required=True,
                            help='This field cannot be blank!'
                            )

        connection = sqlite3.connect('userdata.db')
        cursor = connection.cursor()

        data = parser.parse_args()

        if ItemStorage.find_item_name(self, data['itemname']):
            return {'message': 'This item already exists'}

        query = 'INSERT INTO items VALUES (NULL, ?, ?, ?)'
        cursor.execute(query, (data['itemname'], data['stock'], data['price']))

        connection.commit()
        connection.close()

        return {'message': 'Item stored!'}, 200

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}, 200
