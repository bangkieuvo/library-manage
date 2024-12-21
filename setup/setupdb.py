import sqlite3


conn = sqlite3.connect("../library-manage.db")
cursor = conn.cursor()
sql_file = open("setup.sql","r")
sql = sql_file.read()
for statement in sql.split(";"):
	cursor.execute(statement)
	print(statement)
def deleteTable(name):
	sql = f"""DROP TABLE IF EXISTS {name} """
	conn = sqlite3.connect("../library-manage.db")
	cursor = conn.cursor()
	print(sql)
	cursor.execute(sql)
def deleteAllTable():
	query = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
	tableList = query.fetchall()
	for table in tableList:
		deleteTable(table[0])
#deleteAllTable()