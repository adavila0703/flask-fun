from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from flask import jsonify


class ItemStorage(Resource):
    def __init__(self, itemname, stock, price):
        self.itemname = itemname
        self.stock = stock
        self.price = price

    def find_item(self, itemname):
        connection = sqlite3.connect('userdata.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items WHERE itemname=?'
        result = cursor.execute(query, (itemname,))

        row = result.fetchone()

        if row:
            item = row
        else:
            item = None
        connection.close()
        return item

    def find_all_items(self):
        connection = sqlite3.connect('userdata.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items'
        result = cursor.execute(query)

        templist = []
        tempdict = {}
        for r in result:
            tempdict = {'itemname': r[1], 'stock': r[2], 'price': r[3]}
            templist.append(tempdict)

        connection.close()
        return templist, 200

    def get_single_item(self, itemname):
        connection = sqlite3.connect('userdata.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM items WHERE itemname=?'

        result = cursor.execute(query, (itemname,))
        if result.fetchone() == None:
            return None
        else:
            templist = []
            for r in result:
                print(r)

            return templist, 200


class Item(Resource):
    # @jwt_required()
    def get(self):
        return ItemStorage.find_all_items(self)

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

        data = parser.parse_args()

        if ItemStorage.find_item(self, data['itemname']):
            return {'message': 'This item already exists'}

        connection = sqlite3.connect('userdata.db')
        cursor = connection.cursor()

        query = 'INSERT INTO items VALUES (NULL, ?, ?, ?)'
        cursor.execute(query, (data['itemname'], data['stock'], data['price']))

        connection.commit()
        connection.close()

        return {'message': 'Item stored!'}, 200

    def delete(self):
        parse = reqparse.RequestParser()
        parse.add_argument('itemname',
                           type=str,
                           required=True,
                           help='Itemname is requried!'
                           )
        data = parse.parse_args()

        if ItemStorage.find_item(self, data['itemname']) == None:
            return {'message': 'Item doesnt exist'}

        connection = sqlite3.connect('userdata.db')
        cursor = connection.cursor()

        query = 'DELETE FROM items WHERE itemname=?'

        cursor.execute(query, (data['itemname'],))

        connection.commit()
        connection.close()

        return {'message': 'Item deleted'}, 200

    def put(self):
        parse = reqparse.RequestParser()
        parse.add_argument('itemname',
                           type=str,
                           required=True,
                           help='Itemname field required!')
        parse.add_argument('stock',
                           type=int,
                           required=True,
                           help='Stock field required!')
        parse.add_argument('price',
                           type=int,
                           required=True,
                           help='Price field required!')

        data = parse.parse_args()

        if ItemStorage.find_item(self, data['itemname']):
            connection = sqlite3.connect('userdata.db')
            cursor = connection.cursor()

            query = 'UPDATE items SET stock=?, price=? WHERE itemname=?'

            cursor.execute(query, (data['stock'], data['price'], data['itemname']))

            connection.commit()
            connection.close()
            return {'message': 'Item information updated'}, 200
        else:
            return {'message': 'Item does not exist!'}, 400


class GetSingleItem(Resource):
    def get(self, itemname):
        if ItemStorage.get_single_item(self, itemname):
            return ItemStorage.get_single_item(self, itemname)

