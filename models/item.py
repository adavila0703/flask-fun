import sqlite3

class ItemModel:
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

    def json(self):
        return {'itemname': self.itemname, 'stock': self.stock, 'price': self.stock}