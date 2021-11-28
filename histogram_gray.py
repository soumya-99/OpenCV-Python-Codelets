import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./download.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", img)

dst = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.hist(img.ravel(), 256, [0, 256])
plt.title("Grayscale Histogram")
plt.show()

cv2.destroyAllWindows()