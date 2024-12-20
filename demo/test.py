import tkinter as tk

def show_frame(frame):
    frame.tkraise()  # Hiển thị frame được chọn

root = tk.Tk()
root.geometry("400x300")
root.title("Chuyển đổi giao diện")

# Tạo các Frame
frame1 = tk.Frame(root, bg="lightblue")
frame2 = tk.Frame(root, bg="lightgreen")

for frame in (frame1, frame2):
    frame.place(relwidth=1, relheight=1)

# Nội dung Frame 1
tk.Label(frame1, text="Đây là giao diện 1", bg="lightblue", font=("Arial", 14)).pack(pady=50)
tk.Button(frame1,cursor = "hand2", text="Chuyển sang Giao diện 2", command=lambda: show_frame(frame2)).pack()

# Nội dung Frame 2
tk.Label(frame2, text="Đây là giao diện 2", bg="lightgreen", font=("Arial", 14)).pack(pady=50)
tk.Button(frame2,cursor = "hand2", text="Quay lại Giao diện 1", command=lambda: show_frame(frame1)).pack()

# Hiển thị giao diện đầu tiên
show_frame(frame1)

root.mainloop()
