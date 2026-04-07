import os
import numpy as np
import cv2 as cv
img = cv.imread('input_images/test.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
rows,cols = img.shape
 
# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))

# Lưu hình ảnh
output_dir = 'output_images'
output_path = os.path.join(output_dir, 'rotation_output.jpg')
cv.imwrite(output_path, dst)
print(f"Hình ảnh đã được lưu tại: {output_path}")

cv.imshow('Original', img)
cv.imshow('Rotated',dst)
cv.waitKey(0)
cv.destroyAllWindows()
