import sqlite3
from model import*

class UserDAO:	
	def __init__(self):
		self.conn = sqlite3.connect("library-manage.db")
		self.cursor = self.conn.cursor()
	def __del__(self):
		self.conn.close()
	def isExist(self,id):
		user = self.find(id)
		if user != None:
			return True
		return False
	def find(self,id):
		cursor = self.cursor
		conn = self.conn
		statement = f"select* from user where id = \'{id}\'"
		cursor.execute(statement)
		result = cursor.fetchone()
		if result != None:
			return User(*result)
		return None
	def save(self,user):
		cursor = self.cursor
		conn = self.conn
		if self.isExist(user.id):
			self.update(user)
		else:
			statement = "insert into user values" + str(tuple(vars(user).values()))
			cursor.execute(statement)
			conn.commit()
			print("user is saved!")
	def update(self,user):
		cursor = self.cursor
		conn = self.conn
		if not self.isExist(user.id):
			self.save(user)
			return
		data = tuple(vars(user).values())
		statement = f"""update user 
		set name = ?, hashedPassword = ?  
		where id = \'{user.id}\'"""
		print("user is updated!")
		cursor.execute(statement,(user.name,user.hashedPassword))
		conn.commit()