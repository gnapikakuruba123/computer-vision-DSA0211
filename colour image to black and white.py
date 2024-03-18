import cv2 
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path = r"C:\Users\SRAVAN\Downloads\acdd8297-0cb2-41a9-b9b2-045f9cbb31c8.jpeg"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale",imgGray)
cv2.waitKey(0)
