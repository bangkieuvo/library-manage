import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os



    
# Biến toàn cục để lưu đường dẫn tệp đã chọn
uploaded_file_path = ""

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Tải và lưu tệp")

# Nút để tải tệp
btn_upload = tk.Button(root, text="Tải tệp lên", command=upload_file)
btn_upload.pack(pady=10)

# Nhãn hiển thị đường dẫn tệp
label_file_path = tk.Label(root, text="Chưa có tệp nào được chọn.")
label_file_path.pack(pady=10)



# Chạy ứng dụng
root.mainloop()
