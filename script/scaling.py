import os

import numpy as np
import cv2 as cv
img = cv.imread('input_images/test.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"
res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
#OR
height, width = img.shape[:2]
res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)

# Lưu hình ảnh
output_dir = 'output_images'
output_path = os.path.join(output_dir, 'scaling_output.jpg')
cv.imwrite(output_path, res)
print(f"Hình ảnh đã được lưu tại: {output_path}")

# Display the result
cv.imshow('Original', img)
cv.imshow('Resized', res)
print("Nhấn phím bất kì để đóng cửa sổ...")
cv.waitKey(0)
cv.destroyAllWindows()
