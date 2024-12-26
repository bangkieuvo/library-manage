from service import* 
from datetime import datetime
import tool
def login(userName,password):
	service = UserService()
	user = service.findByUserName(userName)
	if user == None:
		return None
	if user.hashedPassword == tool.encrypt(password):
		return user


def getBorrowingList(user):
	service = BorrowedBookService()
	return service.findBorrowingList(user.id)
def borrowBook(user,bookId):
	bookService = BookService()
	borrowedBookService = BorrowedBookService()
	book = bookService.find(bookId)
	if borrowedBookService.checkBorrowing(user.id,bookId):
		return False
	if book.quantity > 1:
		borrowedBook = BorrowedBook(None,user.id,bookId,datetime.now().strftime("%Y-%m-%d"),0)
		book.quantity -= 1
		print(str(tuple(vars(borrowedBook).values())))
		bookService.save(book)
		borrowedBookService.save(borrowedBook)
		return True
	return False
def returnBook(user,bookId):
	borrowedBookService = BorrowedBookService()
	if !checkBorrowing

returnBook(login("alice01","123456"),1)






 