import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
#
#
# # DDL CREATE TABLE
# cur.execute('''
# 	CREATE TABLE IF NOT EXISTS categories(
# 		id INTEGER PRIMARY KEY AUTOINCREMENT,
# 		name VARCHAR(64) UNIQUE NOT NULL,
# 		is_published BOOLEAN DEFAULT(true)
# 	);
# ''')
# conn.commit()
#
# cur.execute('''
# 	CREATE TABLE IF NOT EXISTS products(
# 		id INTEGER PRIMARY KEY AUTOINCREMENT,
# 		name VARCHAR(128) NOT NULL,
# 		descr VARCHAR(2048),
# 		price DECIMAL(8, 2) NOT NULL,
# 		category_id INTEGER NOT NULL,
# 		FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
# 	);
# ''')
# conn.commit()
#
# # DML INSERT
# cur.executemany('''
# 	INSERT INTO categories(name)
# 	VALUES (?);
# ''', (('Fish', ), ('Drinks', )))
# conn.commit()

# # cur.executemany('''
# # 	INSERT INTO products(name, descr, price, category_id)
# # 	VALUES(?, ?, ?, ?);
# # ''', (('Hamburger', 'With cheese', 100.0, 1), ('Coffee', 'HOT', 50.0, 3)))
# # conn.commit()

# # DML SELECT
# # cur.execute('''
# # 	SELECT * FROM categories
# # 	WHERE is_published = ?;
# # ''', (True, ))
# # print(cur.fetchall())

# # DML UPDATE
# # cur.execute('''
# # 	UPDATE categories
# # 	SET is_published = ?
# # 	WHERE id = ?;
# # ''', (True, 2))
# # conn.commit()

# # DML DELETE
# # cur.execute('''
# # 	DELETE FROM categories
# # 	WHERE is_published = ?;
# # ''', (False, ))
# # conn.commit()

# cur.execute('''
# 	SELECT categories.name, products.name, products.descr, products.price
# 	FROM categories
# 	JOIN products
# 	ON categories.id = products.category_id
# 	WHERE categories.is_published = ?;
# ''', (True, ))
# print(cur.fetchall())

# import psycopg2
#
#
# class Base(object):
#
# 	tablename = None
# 	fields = ()
#
# 	conn = psycopg2.connect('postgresql://belhard:belhard@localhost:5432/bh36d')
# 	cur = conn.cursor()
#
# 	def __init__(self, *args):
# 		self.id = None
# 		args = list(zip(self.fields, args))
# 		for i in args:
# 			self.__setattr__(*i)
# 			self.__getattribute__(i[0])
#
# 	@classmethod
# 	def _refresh(cls) -> int:
# 		cls.cur.execute(f'''
# 			SELECT id FROM {cls.tablename}
# 			ORDER BY id DESC
# 			LIMIT 1;
# 		''')
# 		return cls.cur.fetchone()[0]
#
# 	def save(self) -> None:
# 		if self.id is None:
# 			self.cur.execute(f'''
# 				INSERT INTO {self.tablename}({", ".join(self.fields)})
# 				VALUES({", ".join(['%s' for _ in self.fields])});
# 			''', (self.name, self.is_published))
# 			self.conn.commit()
# 			self.id = self._refresh()
# 		else:
# 			self.cur.execute(f'''
# 				UPDATE {cls.tablename}
# 				SET {", ".join([f"{field} = %s" for field in self.fields])}
# 				WHERE id = %s;
# 			''', ([self.__getattribute__(field) for field in self.fields], self.id))
# 			self.conn.commit()
#
# 	@classmethod
# 	def get(cls, pk: int) -> "Base":
# 		cls.cur.execute(f'''
# 			SELECT {", ".join(cls.fields)} FROM {cls.tablename} WHERE id = %s;
# 		''', (pk, ))
# 		query = cls.cur.fetchone()
# 		if query:
# 			obj = cls(*query)
# 			obj.id = pk
# 			return obj
#
# 	def delete(self):
# 		self.cur.execute(f'''
# 			DELETE FROM {cls.tablename}
# 			WHERE id = %s;
# 		''', (self.id, ))
# 		self.conn.commit()
#
#
# # category = Category('Test2')
# # category.save()
# # print(category.id)
# # cat = Category.get(pk=2)
# # cat.delete()
# # print(cat)
# # cat.name = 'Рыба'
# # cat.is_published = False
# # cat.save()
# # print(cat.name)
# # print(cat.id)
#
#
# class Category(Base):
# 	tablename = 'categories'
# 	fields = ('name', 'is_published')
#
#
# class Product(Base):
# 	tablename = 'products'
# 	fields = ('name', 'descr', 'price', 'category_id')
#
#
# # cat = Category.get(3)
# # print(cat.name)
# # print(Category.fields)
# # cat = Category('food', True)
# # print(cat)
# # print(cat.name)
# cat = Category('Food', True)
# cat.save()