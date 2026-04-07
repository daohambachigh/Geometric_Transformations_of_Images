import os
import numpy as np
import cv2 as cv
import tkinter as tk
from tkinter import filedialog, messagebox

def process_and_scale(image_path, scale_percent):
    img = cv.imread(image_path)
    if img is None:
        print(f"Không thể đọc file: {image_path}")
        return
        
    scale_factor = scale_percent / 100.0
    
    res = cv.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv.INTER_CUBIC)

    # Lưu hình ảnh
    output_dir = 'output_images'
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'scaling_output.jpg')
    cv.imwrite(output_path, res)
    print(f"Hình ảnh đã được lưu tại: {output_path}")

    # Display the result
    cv.imshow('Original', img)
    cv.imshow(f'Resized ({scale_percent}%)', res)
    print("Nhấn phím bất kì để đóng cửa sổ...")
    cv.waitKey(0)
    cv.destroyAllWindows()

def choose_image():
    try:
        scale_percent = float(entry_scale.get())
        if scale_percent <= 0:
            raise ValueError("Tỷ lệ phải lớn hơn 0")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập tỷ lệ % hợp lệ (lớn hơn 0)")
        return

    file_path = filedialog.askopenfilename(
        title="Chọn hình ảnh",
        filetypes=[
            ("Image files", "*.jpg *.jpeg *.png *.bmp *.tif *.tiff"),
            ("All files", "*.*")
        ]
    )
    if file_path:
        process_and_scale(file_path, scale_percent)
    else:
        print("Bạn chưa chọn hình ảnh nào.")

# Tạo cửa sổ giao diện chính
root = tk.Tk()
root.title("Công cụ Scaling Ảnh")
root.geometry("400x250")

# Khung cho ô nhập %
frame_scale = tk.Frame(root)
frame_scale.pack(pady=20)

tk.Label(frame_scale, text="Nhập tỷ lệ resize (%):", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
entry_scale = tk.Entry(frame_scale, font=("Arial", 12), width=10)
entry_scale.insert(0, "200") # Mặc định là x2 (200%)
entry_scale.pack(side=tk.LEFT, padx=5)

# Thêm nút Upload Ảnh
btn_upload = tk.Button(
    root, 
    text="Upload Ảnh & Resize", 
    command=choose_image, 
    font=("Arial", 14), 
    bg="lightgreen", 
    padx=20, 
    pady=10
)
btn_upload.pack(expand=True)

# Khởi chạy vòng lặp sự kiện
root.mainloop()
