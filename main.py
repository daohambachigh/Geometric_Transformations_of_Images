import subprocess
import sys

def show_menu():
    """Hiển thị menu chính"""
    print("\n" + "="*50)
    print("CÔNG CỤ XỬ LÝ BIẾN ĐỔI ẢNH")
    print("="*50)
    print("1. Phép biến đổi Affine (Affine Transform)")
    print("2. Phép biến đổi Perspective (Perspective Transform)")
    print("3. Phép quay ảnh (Rotation)")
    print("4. Phép phóng to/thu nhỏ (Scaling)")
    print("5. Phép tịnh tiến (Translation)")
    print("6. Thoát")
    print("="*50)

def run_script(script_name):
    """Chạy script con"""
    try:
        subprocess.run([sys.executable, script_name], check=True)
    except subprocess.CalledProcessError:
        print(f"Lỗi khi chạy {script_name}")
    except FileNotFoundError:
        print(f"Không tìm thấy file {script_name}")

def main():
    """Chương trình chính"""
    while True:
        show_menu()
        choice = input("Chọn phép biến đổi (1-6): ").strip()
        
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
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1-6")

if __name__ == "__main__":
    main()
