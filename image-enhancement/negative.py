import cv2

img = cv2.imread("./download.jpg")
cv2.imshow("Original", img)

img_inverse = 255 - img
cv2.imshow("Inverse", img_inverse)

cv2.waitKey(0)
cv2.destroyAllWindows()