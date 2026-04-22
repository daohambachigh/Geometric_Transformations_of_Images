Công cụ biến đổi hình ảnh bằng OpenCV, có GUI menu trong main.py.
Tính năng chính
    1. Affine transform (script/affine.py)
    2. Perspective transform (script/perspective.py)
    3. Rotation (script/rotation.py)
    4. Scaling (script/scaling.py)
    5. Translation (script/transformation.py)
Cấu trúc thư mục
    main.py: giao diện chọn chức năng
    script/: các module xử lý
    input_images/: ảnh đầu vào mẫu
    output_images/: ảnh kết quả
Yêu cầu môi trường
    Python 3.x
    Thư viện: opencv-python, numpy, matplotlib (tkinter dùng GUI)
Cài đặt
    Tạo môi trường ảo (khuyến nghị)
    Cài dependencies bằng pip
Cách chạy
    Chạy chương trình chính: python main.py
    Nhập số 1–6 để mở từng chức năng
    Mô tả ngắn thao tác cho từng chức năng (upload ảnh/chọn điểm)
Đầu ra
    Kết quả lưu trong output_images/ với các file: affine_output.jpg, perspective_output.jpg, rotation_output.jpg, scaling_output.jpg, transformation_output.jpg.
Lưu ý sử dụng
    Affine cần chọn đủ 3 điểm nguồn + 3 điểm đích
    Perspective cần chọn đủ 4 điểm
    Nếu không đọc được ảnh, kiểm tra đường dẫn trong input_images/
Hướng phát triển (optional)
    Thêm CLI không cần GUI
    Cho phép chọn đường dẫn output
    Thêm undo/reset tốt hơn cho chọn điểm