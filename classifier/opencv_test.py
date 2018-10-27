import os
import cv2
import numpy as np


# Change Directories
os.chdir('C:\\Users\\peter\\Documents\\Python Scripts\\Color Masking')

# Read Image and Convert to HSV
img = cv2.imread('supersmash.jpg', cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Color Ranges
lower_blue = np.array([110, 10, 50])
upper_blue = np.array([130, 200, 255])
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
lower_grn = np.array([50, 100, 100])
upper_grn = np.array([70, 255, 255])
lower_pink = np.array([115, 100, 50])
upper_pink = np.array([175, 255, 255])
lower_white = np.array([0, 0, 100])
upper_white = np.array([0, 0, 255])

# Masks
mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
mask2 = cv2.inRange(hsv, lower_red, upper_red)
mask3 = cv2.inRange(hsv, lower_grn, upper_grn)
mask4 = cv2.inRange(hsv, lower_pink, upper_pink)
mask5 = cv2.inRange(hsv, lower_white, upper_white)

# Resolved Image
res1 = cv2.bitwise_and(img, img, mask = mask1)
res2 = cv2.bitwise_and(img, img, mask = mask2)
res3 = cv2.bitwise_and(img, img, mask = mask3)
res4 = cv2.bitwise_and(img, img, mask = mask4)
res5 = cv2.bitwise_and(img, img, mask = mask5)
first_res = cv2.bitwise_or(res1, res2)
second_res = cv2.bitwise_or(res4, res3)
third_res = cv2.bitwise_or(first_res, res5)
res = cv2.bitwise_or(third_res, second_res)

# Direct Comparison
cv2.imshow('image', img)
#cv2.imshow('mask', mask)
cv2.imshow('res', res)

# Exit Command
while True:
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()


