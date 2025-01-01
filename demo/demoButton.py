import tkinter as tk

root = tk.Tk()
root.title("Scrollable List Example")
root.geometry("300x400")

# Tạo canvas và scrollbar
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)

# Tạo frame chứa các widget sẽ cuộn
scrollable_frame = tk.Frame(canvas)

# Cập nhật vùng cuộn khi kích thước thay đổi
scrollable_frame.bind(
    "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

# Tạo cửa sổ trong canvas để chứa frame
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Đặt scrollbar vào cửa sổ
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Căn giữa tất cả widget trong scrollable_frame
scrollable_frame.pack_propagate(False)  # Ngừng thay đổi kích thước tự động của frame
scrollable_frame.grid_columnconfigure(0, weight=1, uniform="equal")
scrollable_frame.grid_rowconfigure(0, weight=1, uniform="equal")

# Thêm các widget vào scrollable_frame (danh sách widget)
for i in range(30):
    label = tk.Label(scrollable_frame, text=f"Item {i+1}", font=("Arial", 14))
    label.grid(row=i, column=0, pady=5, padx=5)
    label.grid_configure(sticky="nsew")

# Đảm bảo tất cả các widget trong frame được căn giữa
root.mainloop()
