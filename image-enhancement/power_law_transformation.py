import cv2
import numpy as np

img = cv2.imread("./download.jpg")
cv2.imshow("Original", img)

img2 = img / 255.0
img_power_law = cv2.pow(img2, 1.8)
cv2.imshow("Power Law Transformation", img_power_law)

cv2.waitKey(0)
cv2.destroyAllWindows()