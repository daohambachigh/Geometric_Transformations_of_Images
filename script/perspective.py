import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os

class PointSelector:
    def __init__(self, image_path, num_points=4, label="pts"):
        self.img = cv.imread(image_path)
        if self.img is None:
            print(f"Không tìm thấy ảnh: {image_path}")
            return
        
        self.points = []
        self.num_points = num_points
        self.label = label
        self.window_name = f"Chọn {num_points} điểm ({label}) bằng cách click chuột"
        self.display_img = self.img.copy()
        self.action = None
        self.draw_ui()

    def draw_ui(self):
        """Vẽ các nút lên hiển thị"""
        # Save button
        cv.rectangle(self.display_img, (10, 10), (80, 40), (0, 255, 0), -1)
        cv.putText(self.display_img, "Save", (20, 30), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        
        # Reset button
        cv.rectangle(self.display_img, (90, 10), (170, 40), (0, 255, 255), -1)
        cv.putText(self.display_img, "Reset", (100, 30), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        
        # Quit button
        cv.rectangle(self.display_img, (180, 10), (250, 40), (0, 0, 255), -1)
        cv.putText(self.display_img, "Quit", (190, 30), cv.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
    def mouse_callback(self, event, x, y, flags, param):
        """Xử lý sự kiện chuột"""
        if event == cv.EVENT_LBUTTONDOWN:
            # Kiểm tra click vào nút
            if 10 <= y <= 40:
                if 10 <= x <= 80:
                    self.action = 'save'
                    return
                elif 90 <= x <= 170:
                    self.action = 'reset'
                    return
                elif 180 <= x <= 250:
                    self.action = 'quit'
                    return

            if len(self.points) < self.num_points:
                self.points.append([x, y])
                cv.circle(self.display_img, (x, y), 5, (0, 255, 0), -1)
                cv.putText(self.display_img, f"{len(self.points)}", (x+10, y-10),
                          cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                cv.imshow(self.window_name, self.display_img)
                
                if len(self.points) == self.num_points:
                    print(f"Đã chọn {self.num_points} điểm cho {self.label}!")
    
    def select(self):
        """Bắt đầu chọn điểm"""
        if self.img is None:
            return None
        
        cv.imshow(self.window_name, self.display_img)
        cv.setMouseCallback(self.window_name, self.mouse_callback)
        
        print(f"\nHướng dẫn ({self.label}):")
        print(f"- Click vào {self.num_points} điểm")
        print("- Nhấn 's' hoặc click 'Save' để lưu")
        print("- Nhấn 'r' hoặc click 'Reset' để reset")
        print("- Nhấn 'q' hoặc click 'Quit' để thoát")
        
        while True:
            key = cv.waitKey(10) & 0xFF
            
            # Xử lý sự kiện từ phím hoặc chuột
            if key == ord('s') or self.action == 'save':
                self.action = None
                if len(self.points) == self.num_points:
                    break
                else:
                    print(f"Chỉ chọn được {len(self.points)} điểm, cần {self.num_points} điểm!")
            
            elif key == ord('r') or self.action == 'reset':
                self.action = None
                self.points = []
                self.display_img = self.img.copy()
                self.draw_ui()
                print("Đã reset!")
                cv.imshow(self.window_name, self.display_img)
            
            elif key == ord('q') or self.action == 'quit':
                self.action = None
                print("Hủy chọn!")
                self.points = []
                break
        
        cv.destroyAllWindows()
        return self.points

def calculate_pts2_from_pts1(pts1):
    """Tính pts2 tự động dựa trên khoảng cách các điểm trong pts1"""
    pts1 = np.array(pts1, dtype=np.float32)
    
    # Tính khoảng cách giữa các điểm
    # pts1 = [TL, TR, BL, BR] (top-left, top-right, bottom-left, bottom-right)
    
    # Khoảng cách ngang (từ TL đến TR)
    width = np.linalg.norm(pts1[1] - pts1[0])
    
    # Khoảng cách dọc (từ TL đến BL)
    height = np.linalg.norm(pts1[2] - pts1[0])
    
    # Tạo pts2 là hình chữ nhật đích
    pts2 = np.float32([
        [0, 0],                    # Top-Left
        [width, 0],               # Top-Right
        [0, height],              # Bottom-Left
        [width, height]           # Bottom-Right
    ])
    return pts2

def apply_perspective_transform(image_path, pts1, pts2=None):
    """Áp dụng perspective transform"""
    img = cv.imread(image_path)
    if img is None:
        print(f"Không tìm thấy ảnh: {image_path}")
        return
    
    rows, cols, ch = img.shape
    pts1 = np.float32(pts1)
    
    # Nếu không có pts2, tính tự động từ pts1
    if pts2 is None:
        pts2 = calculate_pts2_from_pts1(pts1)
    else:
        pts2 = np.float32(pts2)
    
    M = cv.getPerspectiveTransform(pts1, pts2)
    
    # Lấy kích thước đích từ pts2
    output_width = int(pts2[1][0] - pts2[0][0])
    output_height = int(pts2[2][1] - pts2[0][1])
    
    dst = cv.warpPerspective(img, M, (output_width, output_height))
    
    # Lưu hình ảnh
    output_dir = 'output_images'
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'perspective_output.jpg')
    cv.imwrite(output_path, dst)
    print(f"Hình ảnh đã được lưu tại: {output_path}")
    
    # Hiển thị kết quả
    plt.figure(figsize=(12, 5))
    plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('Input')
    plt.subplot(122), plt.imshow(cv.cvtColor(dst, cv.COLOR_BGR2RGB)), plt.title('Output')
    plt.show()

def main():
    print("="*50)
    print("   PHÉP BIẾN ĐỔI PERSPECTIVE - CHỌN ĐIỂM TỪ ẢNH")
    print("="*50)
    
    image_path = 'input_images/scan.png'
    
    # Chọn pts1 từ ảnh (4 điểm)
    print("\n>>> Chọn pts1 (4 góc của vùng cần biến đổi)")
    selector1 = PointSelector(image_path, num_points=4, label="pts1")
    pts1 = selector1.select()
    
    if not pts1 or len(pts1) != 4:
        print("❌ Hủy bỏ!")
        return
    
    # pts2 sẽ được tính tự động từ pts1
    print("\n>>> pts2 sẽ được tính tự động từ khoảng cách các điểm...")
    apply_perspective_transform(image_path, pts1)

if __name__ == "__main__":
    main()
