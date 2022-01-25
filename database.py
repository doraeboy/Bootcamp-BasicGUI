#database.py

import sqlite3

conn = sqlite3.connect('product-database.sqlite3')
c = conn.cursor()

# สร้างตาราง * ห้าม Comment ในคำสั่ง """
c.execute("""CREATE TABLE IF NOT EXISTS transaction_history (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				tid TEXT,
				stamp TEXT,
				product TEXT,
				price REAL,
				quan REAL,
				total REAL )""")

print('Success')

#Insert Data
def insert_transaction(data):
	ID = None
	tid = data['tid']
	stamp = data['stamp']
	product = data['product']
	price = data['price']
	quan = data['quan']
	total = data['total']

	with conn:
		command = 'INSERT INTO transaction_history VALUES (?,?,?,?,?,?,?)'
		c.execute(command,(ID,tid,stamp,product,price,quan,total))
		conn.commit()
	print('Insert!')

def view_transaction():
	with conn:
		c.execute("SELECT * FROM transaction_history")
		data = c.fetchall()
		print(data)

transaction = {'tid' : '12341',
				'stamp' : '2022-01-25 20:34:00',
				'product' : 'ทองรูปพรรณ',
				'price' : 25860,
				'quan' : 1,
				'total' : 25860}

#insert_transaction(transaction)

view_transaction()