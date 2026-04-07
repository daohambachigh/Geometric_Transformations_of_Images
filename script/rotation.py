import os
import numpy as np
import cv2 as cv
import tkinter as tk
from tkinter import filedialog

def process_and_rotate(image_path):
    img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Không thể đọc file: {image_path}")
        return
        
    rows,cols = img.shape
     
    # cols-1 and rows-1 are the coordinate limits.
    M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
    dst = cv.warpAffine(img,M,(cols,rows))

    # Lưu hình ảnh
    output_dir = 'output_images'
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'rotation_output.jpg')
    cv.imwrite(output_path, dst)
    print(f"Hình ảnh đã được lưu tại: {output_path}")

    cv.imshow('Original', img)
    cv.imshow('Rotated',dst)
    cv.waitKey(0)
    cv.destroyAllWindows()

def choose_image():
    file_path = filedialog.askopenfilename(
        title="Chọn hình ảnh",
        filetypes=[
            ("Image files", "*.jpg *.jpeg *.png *.bmp *.tif *.tiff"),
            ("All files", "*.*")
        ]
    )
    if file_path:
        process_and_rotate(file_path)
    else:
        print("Bạn chưa chọn hình ảnh nào.")

# Tạo cửa sổ giao diện chính
root = tk.Tk()
root.title("Công cụ Xoay Ảnh (Rotation)")
root.geometry("350x200")

# Thêm nút Upload Ảnh
btn_upload = tk.Button(
    root, 
    text="Upload Ảnh", 
    command=choose_image, 
    font=("Arial", 14), 
    bg="lightblue", 
    padx=20, 
    pady=10
)
btn_upload.pack(expand=True)

# Khởi chạy vòng lặp sự kiện
root.mainloop()
