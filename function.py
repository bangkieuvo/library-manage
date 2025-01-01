from service import* 
from datetime import datetime
import tool
#kiểm tra user có phải admin hay không
def isAdmin(user):
	adminService = AdministratorService()
	admin = adminService.find(user.id)
	if admin != None:
		return True
	return False

#Các tác vụ dành cho tài khoản admin
#input: userId và mã sách muốn mượn
#output: True nếu mượn thành công, False nếu thất bại
def borrowBook(userId,bookId):
	bookService = BookService()
	borrowedBookService = BorrowedBookService()
	book = bookService.find(bookId)
	if borrowedBookService.checkBorrowing(userId,bookId):
		return False
	if book.quantity > 1:
		borrowedBook = BorrowedBook(None,userId,bookId,datetime.now().strftime("%Y-%m-%d"),0)
		book.quantity -= 1
		bookService.save(book)
		borrowedBookService.save(borrowedBook)
		return True
	return False
#input: useId và mã sách cần trả
def returnBook(userId,bookId):
	userService = UserService()
	bookService = BookService()
	borrowedBookService = BorrowedBookService()
	user = userService.find(userId)
	book = bookService.find(bookId)
	borrowedBookList = getBorrowingList(user.id)
	borrowedBook = borrowedBookService.findBorrowingBook(user.id,bookId)
	if borrowedBook != None and book != None:
		print(vars(borrowedBook))
		borrowedBook.isReturned = True
		book.quantity += 1
		bookService.save(book)
		borrowedBookService.save(borrowedBook)


#input: userName và password 
#output: object user nếu đăng nhập thành công, None nếu đăng nhập thất bại 
def login(userName,password):
	service = UserService()
	user = service.findByUserName(userName)
	if user == None:
		return None
	if user.hashedPassword == tool.encrypt(password):
		return user
#input: user và mã sách cần check 
#output: True nếu user đang mượn cuốn sách đó chưa trả, các trường hợp khác trả về False 
def checkBorrowing(userId,bookId):
	borrowedBookService = BorrowedBookService()
	return borrowedBookService.checkBorrowing(userId,bookId)

#input: user 
#output: danh sách các sách mà user đang mượn
def getBorrowingList(userId):
	service = BorrowedBookService()
	return service.findBorrowingList(userId)
#output: danh sách tất cả các cuốn sách trong thư viện
def getBookList(page = 0):
	bookService = BookService()
	books = bookService.findAll()
	if page == 0:
		return books
	return books[10*(page-1):10*(page-1)+10]
#output: danh sách tất cả các cuốn sách có thể cho mượn
def getAllBookAvailable():
	bookService = BookService()
	return list(filter(lambda x: x.quantity > 1, bookService.findAll()))

#output: dach sách tất cả các chủ đề mà thư viện có
def getAllCategory():
	categoryService = CategoryService()
	return categoryService.findAll()
def getBorrowHistory(userId):
	borrowedBookService = BorrowedBookService()
	return borrowedBookService.findHistory(userId)
def getBook(bookId):
	bookService = BookService()
	categoryService = CategoryService()
	book = bookService.find(bookId)
	if book != None:
		book.category = categoryService.find(book.categoryId).name
		return book
def checkAvailableToBorrow(bookId):
	minimumQuantityAlow = 1
	book = getBook(bookId)
	if book:
		if book.quantity > minimumQuantityAlow:
			return True
		else:
			return False
	return False


 