import sqlite3

# 1. Tạo cơ sở dữ liệu và bảng
def create_table():
    # Kết nối đến cơ sở dữ liệu (tạo mới nếu chưa có)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Tạo bảng users nếu chưa tồn tại
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    )
    """)
    conn.commit()
    print("Table created successfully!")

    # Đóng kết nối
    conn.close()

# 2. Thêm dữ liệu vào bảng
def insert_data():
    # Kết nối đến cơ sở dữ liệu
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Thêm một số dữ liệu vào bảng users
    cursor.execute("""
    INSERT INTO users (name, age, email) VALUES (?, ?, ?)
    """, ("Alice", 30, "alice@example.com"))
    cursor.execute("""
    INSERT INTO users (name, age, email) VALUES (?, ?, ?)
    """, ("Bob", 25, "bob@example.com"))

    # Lưu thay đổi
    conn.commit()
    print("Data inserted successfully!")

    # Đóng kết nối
    conn.close()

# 3. Truy vấn dữ liệu
def fetch_data():
    # Kết nối đến cơ sở dữ liệu
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Lấy tất cả dữ liệu từ bảng users
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # In ra các dòng dữ liệu
    print("Fetching data from the users table:")
    for row in rows:
        print(row)

    # Đóng kết nối
    conn.close()

# 4. Cập nhật dữ liệu
def update_data():
    # Kết nối đến cơ sở dữ liệu
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Cập nhật tuổi của Alice
    cursor.execute("""
    UPDATE users
    SET age = ?
    WHERE name = ?
    """, (31, "Alice"))

    # Lưu thay đổi
    conn.commit()
    print("Data updated successfully!")

    # Đóng kết nối
    conn.close()

# 5. Xóa dữ liệu
def delete_data():
    # Kết nối đến cơ sở dữ liệu
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Xóa người dùng Bob
    cursor.execute("""
    DELETE FROM users WHERE name = ?
    """, ("Bob",))

    # Lưu thay đổi
    conn.commit()
    print("Data deleted successfully!")

    # Đóng kết nối
    conn.close()

# 6. Tạo và sử dụng truy vấn có điều kiện
def fetch_data_with_condition():
    # Kết nối đến cơ sở dữ liệu
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Lấy dữ liệu của người dùng có tuổi >= 30
    cursor.execute("SELECT * FROM users WHERE age >= 30")
    rows = cursor.fetchall()

    # In ra kết quả
    print("Users aged 30 or older:")
    for row in rows:
        print(row)

    # Đóng kết nối
    conn.close()

# Chạy các ví dụ
if __name__ == "__main__":
    # create_table()
    # insert_data()
    # fetch_data()
    # update_data()
    # fetch_data()
    # delete_data()
    fetch_data()
    # fetch_data_with_condition()
