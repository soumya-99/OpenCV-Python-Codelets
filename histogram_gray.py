import cv2

img = cv2.imread("./download.jpg")
cv2.imshow("Original", img)

dst = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Rotated by 90 degrees", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()