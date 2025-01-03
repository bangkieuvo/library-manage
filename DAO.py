import sqlite3
from model import*

class UserDAO:	
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

class BorrowedBookDAO:
	def find(self,id):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = f"select* from borrowedBook where id = \'{id}\'"
		cursor.execute(statement)
		result = cursor.fetchone()
		conn.close()
		if result != None:
			return BorrowedBook(*result)
		return None
	def findBorrowingBook(self,userId,bookId):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = f"""select* from borrowedBook where userId = \'{userId}\' 
		and bookId = \'{bookId}\' and isReturned = False"""
		cursor.execute(statement)
		borrowedBook = cursor.fetchone()
		conn.close()
		if borrowedBook != None:
			return BorrowedBook(*borrowedBook)
		return None
	def findByUserId(self,userId,isReturned = None):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		if isReturned != None:
			statement = f"select* from borrowedBook where userId = \'{userId}\' and isReturned = {isReturned}"
		else:
			statement = f"select* from borrowedBook where userId = \'{userId}\'"
		cursor.execute(statement)
		result = cursor.fetchall()
		conn.close()
		listBorrowedBook = []
		for borrowedBook in result:
			listBorrowedBook.append(BorrowedBook(*borrowedBook))
		return listBorrowedBook
	def findAll(self):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = "select* from borrowedBook"
		cursor.execute(statement)
		result = cursor.fetchall()
		conn.close()
		listBorrowedBook = []
		for borrowedBook in result:
			listBorrowedBook.append(BorrowedBook(*borrowedBook))
		return listBorrowedBook
	def save(self,borrowedBook):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = "insert or replace into borrowedBook (userId, bookId, borrowDate, isReturned) values " + str(tuple(vars(borrowedBook).values())[1:])
		cursor.execute(statement)
		conn.commit()
		conn.close()
	def update(self,borrowedBook):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = "insert or replace into borrowedBook values " + str(tuple(vars(borrowedBook).values()))
		cursor.execute(statement)
		conn.commit()
		conn.close()
		print(statement)






class ImageDAO:	
	def find(self,id):
		conn = sqlite3.connect("library-manage.db")
		cursor = conn.cursor()
		cursor.execute("PRAGMA foreign_keys = ON;")
		statement = f"select* from image where id = \'{id}\'"
		cursor.execute(statement)
		result = cursor.fetchone()
		conn.close()
		if result != None:
			return Image(*result)
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


