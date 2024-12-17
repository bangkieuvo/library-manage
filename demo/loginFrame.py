import tkinter as tk
from tkinter import messagebox

# Hàm xử lý khi nhấn nút Đăng nhập
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Kiểm tra tài khoản
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Success", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Login System")
root.geometry("300x200")  # Đặt kích thước cửa sổ

# Tạo Frame cho giao diện đăng nhập
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

# Tạo Label và Entry cho Username
username_label = tk.Label(login_frame, text="Username:")
username_label.grid(row=0, column=0, pady=5, padx=5)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1, pady=5, padx=5)

# Tạo Label và Entry cho Password
password_label = tk.Label(login_frame, text="Password:")
password_label.grid(row=1, column=0, pady=5, padx=5)
password_entry = tk.Entry(login_frame, show="*")  # `show="*"` để ẩn mật khẩu
password_entry.grid(row=1, column=1, pady=5, padx=5)

# Tạo nút Login
login_button = tk.Button(login_frame, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

# Khởi chạy giao diện
root.mainloop()
