import cv2 
import numpy as np

rose = cv2.imread("rosebp.jpg")
rose[200,20] = [255,255,255] 
print(rose[200,50])
cv2.imshow("rose",rose)
(B, G, R) = cv2.split(rose)

cv2.waitKey(0)

# show each channel individually
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

# merge the rose back together again
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# visualize each channel in color
zeros = np.zeros(rose.shape[:2], dtype="uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)


cv2.waitKey(0)