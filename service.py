from DAO import *
class UserService:
	def __init__(self):
		self.dao = UserDAO()
		return
	def find(self,id):
		dao = self.dao
		return dao.find(id)
	def findByUserName(self,userName):
		dao = self.dao
		return dao.findByUserName(userName)
	def findAll(self):
		dao = self.dao
		return dao.findAll()
	def save(self,user):
		dao = self.dao
		dao.save(user)
	def remove(self,user):
		dao = self.dao
		if user != None:
			self.removeById(user.id)
	def removeById(self,id):
		dao = self.dao
		dao.remove(id)
class AdministratorService:
	def __init__(self):
		self.dao = AdministratorDAO()
		return
	def find(self,id):
		dao = self.dao
		return dao.find(id)
	def findAll(self):
		dao = self.dao
		return dao.findAll()
	def save(self,administrator):
		dao = self.dao
		dao.save(administrator)
	def remove(self,administrator):
		dao = self.dao
		if administrator != None:
			self.removeById(administrator.id)
	def removeById(self,id):
		dao = self.dao
		dao.remove(id)
class CategoryService:
	def __init__(self):
		self.dao = CategoryDAO()
		return
	def find(self,id):
		dao = self.dao
		return dao.find(id)
	def findAll(self):
		dao = self.dao
		return dao.findAll()
	def save(self,category):
		dao = self.dao
		dao.save(category)
	def remove(self,category):
		dao = self.dao
		if category != None:
			self.removeById(category.id)
	def removeById(self,id):
		dao = self.dao
		dao.remove(id)
class BookService:
	def __init__(self):
		self.dao = BookDAO()
		return
	def find(self,id):
		dao = self.dao
		return dao.find(id)
	def findAll(self):
		dao = self.dao
		return dao.findAll()
	def save(self,book):
		dao = self.dao
		dao.save(book)
	def remove(self,book):
		dao = self.dao
		if book != None:
			self.removeById(book.id)
	def removeById(self,id):
		dao = self.dao
		dao.remove(id)