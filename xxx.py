from tool import*

for i in range(1,30):
    name = str(i)+".jpg"
    with open("image/"+name, "rb") as file:
        binary_data = file.read()  # Đọc dữ liệu nhị phân
        saveImage(name+"",binary_data)