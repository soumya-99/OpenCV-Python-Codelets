import cv2
img = cv2.imread("./download.jpg")
cv2.imshow("Original", img)
# cv2.waitKey(0)

# # Finding height, width, center X and center Y
# (h, w) = img.shape[:2]
# (cX, cY) = (w // 2, h // 2)

# # Rotate the image by 45 degrees (Anti Clockwise)
# M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0) # (center, angle, scale)

# # Rotate the image by 45 degrees (Clockwise)
# M = cv2.getRotationMatrix2D((cX, cY), -45, 1.0) # (center, angle, scale)

# rotated = cv2.warpAffine(img, M, (w, h))
# cv2.imshow("Rotated by 45 Degrees", rotated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Rotate using Static Fields

# rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# cv2.imshow("Rotated by 90 degrees clockwise", rotated)

rotated_counter = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Rotated by 90 degrees anti-clockwise", rotated_counter)

cv2.waitKey(0)
cv2.destroyAllWindows()