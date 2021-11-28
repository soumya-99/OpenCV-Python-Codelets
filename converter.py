import cv2

img = cv2.imread("./download.jpg")
# img = cv2.resize(img, (600, 400))
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
img = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
# img = cv2.cvtColor(img, cv2)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
