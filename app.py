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
        #messagebox.showinfo("Login Success", "Welcome " + user.name)
        showDashboard(user)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

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
    tk.Button(root, text="Đăng xuất", 
        command=logout, width=30, height=2,cursor = "hand2").pack(pady=20)
def showAdminDashboard(user):
    clear()
    tk.Label(root, text="Xin chào ngài quản trị viên!", font=("Arial", 20)).pack(pady=20)    
    tk.Button(root, text="Thêm tài khoản khách", command=addUser, width=30, height=2).pack(pady=10)
    tk.Button(root, text="View All Books", command=viewAllBooks, width=30, height=2).pack(pady=10)
     
    # Admin can assist normal users with borrowing and returning books
    tk.Button(root, text="Assist with Borrowing Books", command=assistBorrowing, width=30, height=2).pack(pady=10)
    # Logout button
    tk.Button(root, text="Logout", command=logout, width=30, height=2).pack(pady=20)
def showDashboard(user):
    if isAdmin(user):
        showAdminDashboard(user)
    else:
        showUserDashboard(user)

def showBorrowingHistory(user):
    borrowedBooks = getBorrowHistory(user.id)
    bookService = BookService()
    clear()
    tk.Label(root, text=f"Borrowing History for {user.name}", font=("Arial", 20)).pack(pady=20)
    
    for book in borrowedBooks:
        status = "Returned" if book.isReturned else "Not Returned"
        tk.Label(root,cursor = "hand2", text=f"{book.bookId} - {bookService.find(book.bookId).name} - {status} - Borrowed on {book.borrowDate}", font=("Arial", 14)).pack(pady=5)

    tk.Button(root, text="Back", command=lambda: showUserDashboard(user), width=30, height=2).pack(pady=20)

def showBorrowingList(user):
    clear()
    borrowedBooks = getBorrowingList(user.id)
    bookService = BookService()
    tk.Label(root, text=f"Current Borrowing List for {user.name}", font=("Arial", 20)).pack(pady=20)
    
    for book in borrowedBooks:
        if not book.isReturned:
            tk.Label(root, text=f"{book.bookId} - {bookService.find(book.bookId).name} - Borrowed on {book.borrowDate}", font=("Arial", 14)).pack(pady=5)

    tk.Button(root, text="Back", command=lambda: showUserDashboard(user), width=30, height=2).pack(pady=20)
#-------------------------
def editUserInfo(user):
    clear()
    tk.Button(root, text="Thay đổi tên", 
        command=lambda: editUserName(user), 
        width=30, height=2).pack(pady=10)
    tk.Button(root, text="Thay đổi mật khẩu", 
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
    tk.Button(root, text="Lưu thay đổi", command=save, width=30, height=2).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: showUserDashboard(user), width=30, height=2).pack(pady=10)
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
    tk.Button(root, text="Đổi mật khẩu", command=update, width=30, height=2).pack(pady=10)
    tk.Button(root, text="Back", command=lambda: showUserDashboard(user), width=30, height=2).pack(pady=10)

# Function to borrow a book (for users, handled by admin)
def assistBorrowing():
    pass  # Admin can assist normal users in borrowing books

# Function to add a new book (admin action)
def addUser():
    pass  # Implement the functionality to add a new book to the database

def viewBookInfo(bookId, function):
    print(bookId)
    book = getBook(bookId)
    print(vars(book))
    clear()    
    # Sử dụng anchor="w" và width để căn lề trái
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
    
    tk.Button(root, text="Quay lại", command=lambda: function(), width=30, height=2).pack(pady=20)

def viewAllBooks(page = 1):
    books = getBookList(page)
    clear()
    for book in books:        
        tk.Button(root, cursor = "hand2", command = lambda bookId = book.id: viewBookInfo(bookId,lambda:viewAllBooks(page)), 
            text=f"{book.name} -{book.id}- {book.author}", 
            font=("Arial", 14),width = 100,height=2).pack(pady=0)
    if len(getBookList(0)) > 10*page:
        tk.Button(root, text=f"Trang {page+1}", 
            command=lambda: viewAllBooks(page+1), 
            width=10, height=2,cursor = "hand2",).pack(side = "right",padx=0)
    if page > 1:
        tk.Button(root, text=f"Trang {page-1}", 
            command=lambda: viewAllBooks(page-1), 
            width=10, height=2,cursor = "hand2",).pack(side = "left",padx=0)
    tk.Button(root, text="Quay lại", 
        command=lambda: showDashboard(userSession), 
        width=10, height=2).pack(pady=10)
# Function to manage users (admin action)
# Function to log out and return to login screen
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
    loginButton = tk.Button(root, text="Đăng nhập",cursor = "hand2", 
        command = lambda:loginUser(entryUsername.get(),entryPassword.get()), width=30, height=2)
    loginButton.pack(pady=20)
def run():
    loginScreen()
    #loginUser("vbk1212","123456")
    root.mainloop()
run()

