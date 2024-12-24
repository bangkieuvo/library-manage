import sqlite3
from model import*

class UserDAO:	
	def isExist(self,id):
		user = self.find(id)
		if user != None:
			return True
		return False
	def find(self,id):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = f"select* from user where id = \'{id}\'"
		cursor.execute(statement)
		result = cursor.fetchone()
		conn.close()
		if result != None:
			return User(*result)
		return None
	def findByUserName(self,userName):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = f"select* from user where userName = \'{userName}\'"
		cursor.execute(statement)
		result = cursor.fetchone()
		conn.close()
		if result != None:
			return User(*result)
		return None
	def findAll(self):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = "select* from user"
		cursor.execute(statement)
		result = cursor.fetchall()
		conn.close()
		listUser = []
		for user in result:
			listUser.append(User(*user))
		return listUser
	def save(self,user):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = "insert or replace into user values" + str(tuple(vars(user).values()))
		cursor.execute(statement)
		conn.commit()
		conn.close()
		print("user is saved!")
	def remove(self,id):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = f"DELETE FROM user where id = {id}"
		cursor.execute(statement)
		conn.commit()
		conn.close()
		print(f"user with id = {id} is delete!")
class AdministratorDAO:
	def isExist(self,id):
		admin = self.find(id)
		if admin != None:
			return True
		return False
	def find(self,id):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = f"select* from administrator where id = \'{id}\'"
		cursor.execute(statement)
		result = cursor.fetchone()
		conn.close()
		if result != None:
			return Administrator(*result)
		return None
	def findAll(self):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = "select* from administrator"
		cursor.execute(statement)
		result = cursor.fetchall()
		conn.close()
		listAdmin = []
		for admin in result:
			listAdmin.append(Administrator(*admin))
		return listAdmin
	def save(self,admin):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		if self.isExist(admin.id):
			return
		statement = f"insert into administrator values ({admin.id})"	
		cursor.execute(statement)
		conn.commit()
		conn.close()
		print("admin is saved!")
	def remove(self,id):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = f"DELETE FROM administrator where id = {id};"
		cursor.execute(statement)
		conn.commit()
		conn.close()
		print(f"admin with id = {id} is delete!")
class CategoryDAO:
	def isExist(self,id):
		category = self.find(id)
		if category != None:
			return True
		return False
	def find(self,id):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = f"select* from category where id = \'{id}\'"
		cursor.execute(statement)
		result = cursor.fetchone()
		conn.close()
		if result != None:
			return Category(*result)
		return None
	def findAll(self):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = "select* from category"
		cursor.execute(statement)
		result = cursor.fetchall()
		conn.close()
		listCategory = []
		for category in result:
			listCategory.append(Category(*category))
		return listCategory
	def save(self,category):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = "insert or replace into category values" + str(tuple(vars(category).values()))
		cursor.execute(statement)
		conn.commit()
		conn.close()
		print("category is saved!")
class BookDAO:
	def isExist(self,id):
		book = self.find(id)
		if book != None:
			return True
		return False
	def find(self,id):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = f"select* from book where id = \'{id}\'"
		cursor.execute(statement)
		result = cursor.fetchone()
		conn.close()
		if result != None:
			return Book(*result)
		return None
	def findAll(self):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = "select* from book"
		cursor.execute(statement)
		result = cursor.fetchall()
		conn.close()
		listBook = []
		for book in result:
			listBook.append(Book(*book))
		return listBook
	def save(self,book):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = "insert or replace into book values " + str(tuple(vars(book).values()))
		cursor.execute(statement)
		conn.commit()
		conn.close()
		print(f"book with id = {book.id} is saved!")










