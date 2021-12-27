import cv2

img = cv2.imread("./download.jpg")
# img = cv2.imread("./download.jpg", 0)

# img = cv2.resize(img, (600, 400))
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img_converted = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# img_converted = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
# img_converted = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# img_converted = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
# img_converted = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
# img_converted = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
img_converted = cv2.cvtColor(img, cv2.COLOR_YCrCb2RGB)
# img_converted = cv2.cvtColor(img, cv2)
# ret, binary_image = cv2.threshold(img, 127, 256, cv2.THRESH_BINARY)

cv2.imshow("image", img_converted)
# cv2.imshow("image", binary_image)
cv2.imwrite("./download_converted.jpg", img_converted)
# cv2.imwrite("./download_converted_bin.jpg", binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
