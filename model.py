class User:
	def __init__(self,id,name,userName,hashedPassword):
		self.id = id
		self.name = name
		self.userName = userName
		self.hashedPassword = hashedPassword
class Category:
	def __init__(self,id,name,description):
		self.id = id
		self.name = name 
		self.description = description
class Book:
	def __init__(self,bookCode,name,categoryId,quantity):
		self.id = bookCode
		self.name = name
		self.categoryId = categoryId
		self.quantity = quantity 
class Administrator:
	def __init__(self,id):
		self.id = id

	