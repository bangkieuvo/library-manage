import tkinter as tk
from PIL import Image, ImageTk
def button_clicked(n):
    for i in range(n):
        print("Button clicked!")

root = tk.Tk()
root.geometry("5000x5000")
root.title("Demo button")
# Creating a button with specified options
image = Image.open("../picture/book.jpeg")  # Đường dẫn đến ảnh
resized_image = image.resize((275, 183))  # Thay đổi kích thước nếu cần
img = ImageTk.PhotoImage(resized_image)
button = tk.Button(root, 
                   image = img,
                   text="Click Me", 
                   command=lambda:button_clicked(7),
                   compound="bot",
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=500,
                   heigh = 400,
                   wraplength=100)

button.pack(padx=20, pady=20)

root.mainloop()