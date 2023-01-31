import sqlite3
from csv import DictReader, DictWriter

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

# cur.execute('''
# 	CREATE TABLE IF NOT EXISTS categories(
# 		id INTEGER PRIMARY KEY AUTOINCREMENT,
# 		name VARCHAR(24) UNIQUE NOT NULL
# 	);
# ''')
# conn.commit()
#
# cur.execute('''
# 	CREATE TABLE IF NOT EXISTS users(
# 		id INTEGER PRIMARY KEY AUTOINCREMENT,
# 		name VARCHAR(24) UNIQUE NOT NULL,
# 		email VARCHAR(24) UNIQUE NOT NULL
# 	);
# ''')
# conn.commit()
#
# cur.execute('''
# 	CREATE TABLE IF NOT EXISTS statuses(
# 		id INTEGER PRIMARY KEY AUTOINCREMENT,
# 		name VARCHAR(10) UNIQUE NOT NULL
# 	);
# ''')
# conn.commit()
#
# cur.execute('''
# 	CREATE TABLE IF NOT EXISTS products(
# 		id INTEGER PRIMARY KEY AUTOINCREMENT,
# 		title VARCHAR(36) NOT NULL,
# 		description VARCHAR(140),
# 		price DECIMAL(8,2) NOT NULL,
# 		category_id INTEGER NOT NULL,
# 		FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
# 	);
# ''')
# conn.commit()
#
# cur.execute('''
# 	CREATE TABLE IF NOT EXISTS orders(
# 		id INTEGER PRIMARY KEY AUTOINCREMENT,
# 		user_id INTEGER NOT NULL,
# 		status_id INTEGER NOT NULL,
# 		FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
# 		FOREIGN KEY (status_id) REFERENCES statuses(id) ON DELETE CASCADE
# 	);
# ''')
# conn.commit()
#
# cur.execute('''
# 	CREATE TABLE IF NOT EXISTS order_items(
# 		id INTEGER PRIMARY KEY AUTOINCREMENT,
# 		order_id INTEGER NOT NULL,
# 		product_id INTEGER NOT NULL,
# 		FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
# 		FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
# 	);
# ''')
# conn.commit()
#
# cur.executemany('''
# 	INSERT INTO categories(name)
# 	VALUES (?);
# ''', (('Vegetables', ), ('Fruits', )))
# conn.commit()
#
# cur.executemany('''
# 	INSERT INTO products(title, description, price, category_id)
# 	VALUES(?, ?, ?, ?);
# ''', (('Tomato', 'Red', 6.0, 1), ('Apple', 'Yellow', 2.0, 2), ('Pepper', 'Red', 3.0, 1)))
# conn.commit()
#
# cur.executemany('''
# 	INSERT INTO statuses(name)
# 	VALUES(?);
# ''', (('Ready', ), ("Don't ready", )))
# conn.commit()
#
# cur.executemany('''
# 	INSERT INTO users(name, email)
# 	VALUES(?, ?);
# ''', (('Vasya', '111@info.by'), ('Masha', '222@info.by'), ('Lena', '333@info.by')))
# conn.commit()
#
# cur.executemany('''
# 	INSERT INTO orders(user_id, status_id)
# 	VALUES(?, ?);
# ''', ((1, 1), (2, 2)))
# conn.commit()
#
# cur.executemany('''
# 	INSERT INTO order_items(order_id, product_id)
# 	VALUES(?, ?);
# ''', ((1, 2), (2, 1)))
# conn.commit()

#    JOIN
cur.execute('''
    SELECT products.title, categories.name FROM order_items
    JOIN orders ON order_items.order_id = orders.id
    JOIN products ON order_items.product_id = products.id
    JOIN categories ON products.category_id = categories.id
    WHERE order_items.product_id = 1;
''')
print(cur.fetchall())

def upload_from_csv(file: str):
    with open(file, 'r', encoding='utf-8') as file:
        reader = DictReader(file)
        for product in reader:
            cur.execute('''
                INSERT INTO products(title, description, price, category_id)
	            VALUES(?, ?, ?, ?);
''', (product['title'], product['description'], product['price'], product['category_id']))
            try:
                conn.commit()
            except sqlite3.IntegrityError:
                print('IntegrityError')

upload_from_csv('prod.csv')


def save_to_csv(file: str):
    cur.execute('''SELECT id, title, description, price, category_id FROM products''')
    products = [
        {
            'id': product[0],
            'title': product[1],
            'description': product[2],
            'price': product[3],
            'category_id': product[4]
        }
        for product in cur.fetchall()
    ]
    with open(file, 'w', encoding='utf-8') as file:
        writer = DictWriter(file, fieldnames=('id', 'title', 'description', 'price', 'category_id'))
        writer.writeheader()
        writer.writerows(products)

save_to_csv('prod_to_csv.csv')






