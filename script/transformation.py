import os
import numpy as np
import cv2 as cv
img = cv.imread('input_images/logo.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"
rows,cols = img.shape[:2]
M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()
# Lưu hình ảnh
output_dir = 'output_images'
output_path = os.path.join(output_dir, 'transformation_output.jpg')
cv.imwrite(output_path, dst)
print(f"Hình ảnh đã được lưu tại: {output_path}")