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
#input: user và mã sách muốn mượn
#output: True nếu mượn thành công, False nếu thất bại
def borrowBook(user,userId,bookId):
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
def checkBorrowing(user,bookId):
	borrowedBookService = BorrowedBookService()
	return borrowedBookService.checkBorrowing(user.id,bookId)

#input: user 
#output: danh sách các sách mà user đang mượn
def getBorrowingList(user):
	service = BorrowedBookService()
	return service.findBorrowingList(user.id)



#input: user và mã sách cần trả
def returnBook(user,bookId):
	bookService = BookService()
	borrowedBookService = BorrowedBookService()
	book = bookService.find(bookId)
	borrowedBookList = getBorrowingList(user)
	borrowedBook = borrowedBookService.findBorrowingBook(user.id,bookId)
	if borrowedBook != None and book != None:
		print(vars(borrowedBook))
		borrowedBook.isReturned = True
		book.quantity += 1
		bookService.save(book)
		borrowedBookService.save(borrowedBook)

#output: danh sách tất cả các cuốn sách trong thư viện
def getAllBook():
	bookService = BookService()
	return bookService.findAll()
#output: danh sách tất cả các cuốn sách có thể cho mượn
def getAllBookAvailable():
	bookService = BookService()
	return list(filter(lambda x: x.quantity > 1, bookService.findAll()))
#output: dach sách tất cả các chủ đề mà thư viện có
def getAllCategory():
	categoryService = CategoryService()
	return categoryService.findAll()


 