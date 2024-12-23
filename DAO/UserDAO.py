import sqlite3
from ..model import User
conn = sqlite3.connect("../library-manage.db")
cursor = conn.cursor()

def findUser(id):
	statement = f"select* from user where id = \'{id}\'"
	cursor.execute(statement)
	result = cursor.fetchone()
	return User(result)
def updateUser(user):
	statement = f"update user set id = {user.id} where id = \'{id}\'"
u = findUser(1)