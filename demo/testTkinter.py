import tkinter as tk
from PIL import Image, ImageTk
image = Image.open("../picture/book.jpeg")  # Đường dẫn đến ảnh
print(image.size)