import tkinter as tk
from tkinter import messagebox
from service import *
from datetime import datetime
from function import *
from tool import *
# Initialize the main window
root = tk.Tk()
root.title("Hệ thống quản lí thư viện")

# Set the window size
root.geometry("1000x1000")


userSession = None
def clear():
    for widget in root.winfo_children():
        widget.destroy()

def loginUser(username, password):
    user = login(username, password)
    global userSession
    userSession = user 
    if user:
        messagebox.showinfo("Đăng nhập thành công!", "Chào mừng đến với thư viện " + user.name+"!")
        showDashboard(user)
    else:
        messagebox.showerror("Đăng nhập thất bại", "Sai thông tin đăng nhập")

def showUserDashboard(user):
    clear()
    tk.Label(root, text="Chào mừng đến với hệ thống quản lí thư viện " + user.name, 
        font=("Arial", 20)).pack(pady=20)    

    tk.Button(root, cursor = "hand2", 
        text="Xem danh sách sách trong thư viện", 
        command=viewAllBooks, 
        width=30, height=2).pack(pady=10)
    tk.Button(root, cursor = "hand2", 
        text="Xem lịch sử mượn sách", 
        command=lambda: showBorrowingHistory(user), 
        width=30, height=2).pack(pady=10)
    tk.Button(root, cursor = "hand2", 
        text="Xem danh sách đang mượn", 
        command=lambda: showBorrowingList(user), 
        width=30, height=2).pack(pady=10)
    tk.Button(root, cursor = "hand2", 
        text="Sửa thông tin", 
        command=lambda: editUserInfo(user), 
        width=30, height=2).pack(pady=10)
    tk.Button(root, cursor = "hand2",  text="Đăng xuất", 
        command=logout, width=30, height=2).pack(pady=20)
def showAdminDashboard(user):
    clear()
    tk.Label(root, text="Xin chào ngài quản trị viên!", font=("Arial", 20)).pack(pady=20)    
    tk.Button(root, cursor = "hand2",  text="Tạo tài khoản khách", command=addUser, width=30, height=2).pack(pady=10)
    tk.Button(root, cursor = "hand2",  text="Thêm sách", command=addBook, width=30, height=2).pack(pady=10)
    tk.Button(root, cursor = "hand2",  text="Xem danh sách sách trong thư viện", command=viewAllBooks, width=30, height=2).pack(pady=10)
     
    # Admin can assist normal users with borrowing and returning books
    tk.Button(root, cursor = "hand2",  text="Cho người dùng mượn sách", command=assistBorrowing, width=30, height=2).pack(pady=10)
    # Logout button
    tk.Button(root, cursor = "hand2",  text="Đăng xuất", command=logout, width=30, height=2).pack(pady=20)
def showDashboard(user):
    if isAdmin(user):
        showAdminDashboard(user)
    else:
        showUserDashboard(user)

def showBorrowingHistory(user):
    borrowedBooks = getBorrowHistory(user.id)
    bookService = BookService()
    clear()
    tk.Label(root, text=f"Lịch sử mượn sách của {user.name}", font=("Arial", 20)).pack(pady=20)
    
    for book in borrowedBooks:
        status = "Đã trả" if book.isReturned else "Chưa trả"
        tk.Label(root,cursor = "hand2", text=f"{book.bookId} - {bookService.find(book.bookId).name} - {status} - Ngày mượn: {book.borrowDate}", font=("Arial", 14)).pack(pady=5)

    tk.Button(root, cursor = "hand2",  text="Back", command=lambda: showUserDashboard(userSession), width=30, height=2).pack(pady=20)

def showBorrowingList(user):
    clear()
    borrowedBooks = getBorrowingList(user.id)
    bookService = BookService()
    tk.Label(root, text=f"Danh sách đang mượn của {user.name}", font=("Arial", 20)).pack(pady=20)
    
    for book in borrowedBooks:
        if not book.isReturned:
            tk.Label(root, text=f"{book.bookId} - {bookService.find(book.bookId).name} - ngày mượn: {book.borrowDate}", font=("Arial", 14)).pack(pady=5)

    tk.Button(root, cursor = "hand2",  text="Back", command=lambda: showUserDashboard(userSession), width=30, height=2).pack(pady=20)
#-------------------------
def editUserInfo(user):
    clear()
    tk.Button(root, cursor = "hand2",  text="Thay đổi tên", 
        command=lambda: editUserName(user), 
        width=30, height=2).pack(pady=10)
    tk.Button(root, cursor = "hand2",  text="Thay đổi mật khẩu", 
        command=lambda: editUserPassword(user), 
        width=30, height=2).pack(pady=10)
def editUserName(user):
    clear()
    tk.Label(root, text="Tên: ", font=("Arial", 14)).pack(pady=10)

    entryName = tk.Entry(root, font=("Arial", 14))
    entryName.insert(0, f"{user.name}")
    entryName.pack(pady=10)
    userService = UserService()
    def save():
        user.name = entryName.get()
        userService.save(user)
    tk.Button(root, cursor = "hand2",  text="Lưu thay đổi", command=save, width=30, height=2).pack(pady=10)
    tk.Button(root, cursor = "hand2",  text="Back", command=lambda: showUserDashboard(userSession), width=30, height=2).pack(pady=10)
def editUserPassword(user):
    clear()
    tk.Label(root, text="Nhập mật khẩu cũ: ", font=("Arial", 14)).pack(pady=10)
    
    entryOldPassword = tk.Entry(root, font=("Arial", 14))
    entryOldPassword.pack(pady=10)

    entryNewPassword = tk.Entry(root, font=("Arial", 14))
    entryNewPassword.pack(pady=10)

    entryNewPassword2 = tk.Entry(root, font=("Arial", 14))
    entryNewPassword2.pack(pady=10)

    userService = UserService()
    def check(old, new, new2):
        if new != new2:
            return 0
        u = login(user.userName, old)
        if u == None:
            return -1
        return 1
    def update():
        oldPw = entryOldPassword.get()
        newPw = entryNewPassword.get()
        newPw2 = entryNewPassword2.get()
        checkCode = check(oldPw, newPw, newPw2)
        if checkCode == 0:
            messagebox.showerror("Thất bại", "Mật khẩu mới không khớp!")
        elif checkCode == -1:
            messagebox.showerror("Thất bại", "Nhập sai mật khẩu cũ!")
        else:
            user.hashedPassword = encrypt(newPw)
            userService.save(user)
            messagebox.showinfo("Thành công", "Thay đổi mật khẩu thành công!")
    tk.Button(root, cursor = "hand2",  text="Đổi mật khẩu", command=update, width=30, height=2).pack(pady=10)
    tk.Button(root, cursor = "hand2",  text="Back", command=lambda: showUserDashboard(userSession), width=30, height=2).pack(pady=10)

def addBook()
def assistBorrowing():
    clear()
    tk.Label(root, text="Nhập mã người mượn: ", font=("Arial", 14)).pack(pady=10)
    entryBorrowerId = tk.Entry(root, font=("Arial", 14))
    entryBorrowerId.pack(pady=10)

    tk.Label(root, text="Nhập mã sách: ", font=("Arial", 14)).pack(pady=10)
    entryBookId = tk.Entry(root, font=("Arial", 14))
    entryBookId.pack(pady=10)
    def borrow():
        borrowerId = entryBorrowerId.get()
        bookId = entryBookId.get()
        check = borrowBook(borrowerId,bookId)
        if not check:
            messagebox.showerror("Thất bại", "Kiểm tra lại thông tin!")
            assistBorrowing()
        else:
            messagebox.showinfo("Thành công", "Đã cho mượn thành công!")
    tk.Button(root, cursor = "hand2",  text="Cho mượn", command=borrow, width=30, height=2).pack(pady=10)      
    tk.Button(root, cursor = "hand2",  text="Quay lại", command=lambda: showAdminDashboard(userSession), width=30, height=2).pack(pady=10)      

# Function to add a new book (admin action)
def addUser():
    clear()
    userId = generateUserId()
    tk.Label(root, text=f"id: {userId} ", font=("Arial", 20)).pack(pady=10)    
    
    tk.Label(root, text="Nhập tên: ", font=("Arial", 14)).pack(pady=10)
    entryName = tk.Entry(root, font=("Arial", 14))
    entryName.pack(pady=10)

    tk.Label(root, text="Nhập tên đăng nhập: ", font=("Arial", 14)).pack(pady=10)
    entryUserName = tk.Entry(root, font=("Arial", 14))
    entryUserName.pack(pady=10)

    tk.Label(root, text="Nhập mật khẩu: ", font=("Arial", 14)).pack(pady=10)
    entryPassword = tk.Entry(root,show = "*", font=("Arial", 14))
    entryPassword.pack(pady=10)

    tk.Label(root, text="Nhập lại mật khẩu: ", font=("Arial", 14)).pack(pady=10)
    entryPassword2 = tk.Entry(root,show = "*", font=("Arial", 14))
    entryPassword2.pack(pady=10)

    def add():
        name = entryName.get()
        if len(name) == 0:
            messagebox.showerror("Tạo tài khoản thất bại!","Vui lòng nhập tên!")
            addUser()
            return
        userName = entryUserName.get()
        if len(userName) == 0:
            messagebox.showerror("Tạo tài khoản thất bại!","Vui lòng nhập tên đăng nhập!")
            addUser()
            return
        password = entryPassword.get()
        if len(password) == 0:
            messagebox.showerror("Tạo tài khoản thất bại!","Vui lòng nhập mật khẩu!")
            addUser()
            return
        password2 = entryPassword2.get()
        if len(password) == 0:
            messagebox.showerror("Tạo tài khoản thất bại!","Vui lòng nhập lại mật khẩu!")
            addUser()
            return
        userService = UserService()
        user = userService.findByUserName(userName)
        if user != None:
            messagebox.showerror("Tạo tài khoản thất bại!","Tên đăng nhập đã tồn tại!")
            addUser()
            return
        if password != password2:
            messagebox.showerror("Tạo tài khoản thất bại!","Mật khẩu nhập lại không khớp!")
            addUser()
            return
        newUser = User(userId,name,userName,encrypt(password))
        userService.save(newUser)  
        messagebox.showinfo("Thành công","Tạo tài khoản thành công!")
        showAdminDashboard(userSession)
    tk.Button(root, cursor = "hand2",  text="Tạo tài khoản", command=add, width=30, height=2).pack(pady=10)
    tk.Button(root, cursor = "hand2",  text="Quay lại", command=lambda: showAdminDashboard(userSession), width=30, height=2).pack(pady=10)      
def viewBookInfo(bookId, function):
    book = getBook(bookId)
    clear()    
    label_image = tk.Label(root)
    label_image.pack()
    image = getImage(book.id)
    image = image.resize((200, 300), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(image)
    label_image.config(image=tk_image)
    label_image.image = tk_image
    tk.Label(root, text=f"Mã sách: {book.id}", 
             font=("Arial", 20), anchor="w", width=50).pack(pady=5)
    tk.Label(root, text=f"Tên sách: {book.name}", 
             font=("Arial", 20), anchor="w", width=50).pack(pady=5)
    tk.Label(root, text=f"Tác giả: {book.author}", 
             font=("Arial", 20), anchor="w", width=50).pack(pady=5)
    tk.Label(root, text=f"Thể loại: {book.category}", 
             font=("Arial", 20), anchor="w", width=50).pack(pady=5)
    tk.Label(root, text=f"Số lượng có sẵn: {book.quantity}", 
             font=("Arial", 20), anchor="w", width=50).pack(pady=5)
    if checkAvailableToBorrow(book.id):
        status = "Có thể cho mượn"
    else:
        status = "Không thể cho mượn"
    tk.Label(root, text=f"Tình trạng: {status}", 
             font=("Arial", 20), anchor="w", width=50).pack(pady=5)
    
    tk.Button(root, cursor = "hand2",  text="Quay lại", command=lambda: function(), width=30, height=2).pack(pady=20)

def viewAllBooks(page = 1):
    books = getBookList(page)
    clear()
    for book in books:        
        tk.Button(root, cursor = "hand2",  command = lambda bookId = book.id: viewBookInfo(bookId,lambda:viewAllBooks(page)), 
            text=f"{book.name} - {book.author}", 
            font=("Arial", 14),width = 100,height=2).pack(pady=0)
    if len(getBookList(0)) > 10*page:
        tk.Button(root, cursor = "hand2",  text=f"Trang {page+1}", 
            command=lambda: viewAllBooks(page+1), 
            width=10, height=2).pack(side = "right",padx=0)
    if page > 1:
        tk.Button(root, cursor = "hand2",  text=f"Trang {page-1}", 
            command=lambda: viewAllBooks(page-1), 
            width=10, height=2).pack(side = "left",padx=0)
    tk.Button(root, cursor = "hand2",  text="Quay lại", 
        command=lambda: showDashboard(userSession), 
        width=10, height=2).pack(pady=10)
def logout():
    global userSession
    userSession = None
    loginScreen()
def loginScreen():
    clear()
    tk.Label(root,anchor = "center", text="Tên đăng nhập", font=("Arial", 14)).pack(pady=10)
    entryUsername = tk.Entry(root, font=("Arial", 14))
    entryUsername.pack(pady=10)

    tk.Label(root, text="Mật khẩu", font=("Arial", 14)).pack(pady=10)
    entryPassword = tk.Entry(root, show="*", font=("Arial", 14))
    entryPassword.pack(pady=10)
    loginButton = tk.Button(root, cursor = "hand2",  text="Đăng nhập", 
        command = lambda:loginUser(entryUsername.get(),entryPassword.get()), width=30, height=2)
    loginButton.pack(pady=20)
def run():
    #loginScreen()
    loginUser("vbk1212","123456")
    root.mainloop()
run()

