import cv2
import numpy as np

img = cv2.imread("./rgb_image.jpg", 0)
cv2.imshow("Original", img)

img_log_law_transformed = 0.6 * np.log(1 + np.float32(img))

cv2.imshow("Log Law Transformed", img_log_law_transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()