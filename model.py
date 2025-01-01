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
	def __init__(self,bookCode,name,author,categoryId,quantity):
		self.id = bookCode
		self.name = name
		self.author = author
		self.categoryId = categoryId
		self.quantity = quantity 
class Administrator:
	def __init__(self,id):
		self.id = id
class BorrowedBook:
	def __init__(self,id,userId,bookId,borrowDate,isReturned):
		self.id = id
		self.userId = userId
		self.bookId = bookId
		self.borrowDate = borrowDate
		self.isReturned = isReturned

	