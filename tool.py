def encrypt(cipher):
	import hashlib
	sha256 = hashlib.sha256()
	sha256.update(cipher.encode("utf-8"))
	return sha256.hexdigest()

def generateUserId():
    import sqlite3
    conn = sqlite3.connect("library-manage.db")
    cursor = conn.cursor()
    statement = f"select id from user order by id desc limit 1"
    cursor.execute(statement)
    result = cursor.fetchone()
    conn.close()
    return result[0] + 1 


import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import sqlite3

# Kết nối SQLite



# Hàm lưu ảnh vào SQLite
def selectImage():
    conn = sqlite3.connect("library-manage.db")
    cursor = conn.cursor()
    # Chọn tệp ảnh
    file_path = filedialog.askopenfilename(
        title="Chọn ảnh",
        filetypes=[("Ảnh", "*.jpg")]
    )
    if file_path:
        
        with open(file_path, "rb") as file:
            binary_data = file.read()  # Đọc dữ liệu nhị phân
            
        # Lưu vào cơ sở dữ liệu
        cursor.execute("INSERT or replace INTO image (name, data) VALUES (?, ?)", 
                       (file_path.split("/")[-1], binary_data))
        conn.commit()
    conn.close()
def saveImage(name,imageData):
    conn = sqlite3.connect("library-manage.db")

    cursor = conn.cursor()
    
    cursor.execute("INSERT or replace INTO image (name, data) VALUES (?, ?)", 
                   (name, imageData))
    conn.commit()
    conn.close()

def getImage(name = 21):
    import io
    conn = sqlite3.connect("library-manage.db")
    cursor = conn.cursor()
    # Lấy ảnh từ cơ sở dữ liệu
    sql = f"SELECT data FROM image where name = \'{name}.jpg\'"
    cursor.execute(sql)
    row = cursor.fetchone()
    if row is None:
       return None
    binary_data = row[0]  # Lấy dữ liệu nhị phân
    img = Image.open(io.BytesIO(binary_data))
    conn.close()
    return img
