import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

def run_script(script_name):
    """Chạy script con"""
    try:
        # Sử dụng Popen để chạy script mà không làm đơ giao diện chính
        subprocess.Popen([sys.executable, script_name])
    except Exception as e:
        messagebox.showerror("Lỗi", f"Không thể chạy {script_name}\nChi tiết: {e}")

def main():
    """Chương trình chính với giao diện GUI"""
    root = tk.Tk()
    root.title("Công Cụ Xử Lý Biến Đổi Ảnh")
    root.geometry("450x380")

    # Tiêu đề
    lbl_title = tk.Label(root, text="CÔNG CỤ XỬ LÝ BIẾN ĐỔI ẢNH", font=("Arial", 16, "bold"))
    lbl_title.pack(pady=15)

    # Hiển thị danh sách Menu ngay trong cửa sổ
    menu_text = (
        "1. Phép biến đổi Affine (Affine Transform)\n\n"
        "2. Phép biến đổi Perspective (Perspective Transform)\n\n"
        "3. Phép quay ảnh (Rotation)\n\n"
        "4. Phép phóng to/thu nhỏ (Scaling)\n\n"
        "5. Phép tịnh tiến (Translation)\n\n"
        "6. Thoát"
    )
    lbl_menu = tk.Label(root, text=menu_text, font=("Arial", 12), justify="left")
    lbl_menu.pack(pady=5)

    # Hàm xử lý khi ấn nút hoặc phím Enter
    def execute_choice(event=None):
        choice = entry_choice.get().strip()
        if choice == '1':
            run_script('script/affine.py')
        elif choice == '2':
            run_script('script/perspective.py')
        elif choice == '3':
            run_script('script/rotation.py')
        elif choice == '4':
            run_script('script/scaling.py')
        elif choice == '5':
            run_script('script/transformation.py')
        elif choice == '6':
            root.quit()
        else:
            messagebox.showwarning("Lỗi", "Lựa chọn không hợp lệ!\nVui lòng nhập số từ 1 đến 6.")
        
        # Xóa nội dung ô nhập sau khi chạy
        entry_choice.delete(0, tk.END)

    # Khung nhập liệu (hộp chat nhập số)
    frame_input = tk.Frame(root)
    frame_input.pack(pady=20)

    lbl_input = tk.Label(frame_input, text="Nhập số (1-6):", font=("Arial", 12, "bold"))
    lbl_input.pack(side=tk.LEFT, padx=5)

    entry_choice = tk.Entry(frame_input, font=("Arial", 14), width=5, justify="center")
    entry_choice.pack(side=tk.LEFT, padx=5)
    # Ràng buộc phím Enter với hàm xử lý
    entry_choice.bind('<Return>', execute_choice)

    btn_run = tk.Button(frame_input, text="Chạy", font=("Arial", 12, "bold"), bg="lightblue", command=execute_choice)
    btn_run.pack(side=tk.LEFT, padx=10)

    # Tự động focus con trỏ vào ô nhập
    entry_choice.focus()

    root.mainloop()

if __name__ == "__main__":
    main()
