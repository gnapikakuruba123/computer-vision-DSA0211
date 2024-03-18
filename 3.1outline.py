import cv2
import numpy as np
kerner=np.ones((5,5),np.unit8)
print(kernel)
path= r"C:\Users\SRAVAN\Downloads\pexels-pixabay-371285.jpg"
img =cv2.imread(path)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv2.canny(imgBlur,100,200)
cv2.imshow("imgCanny",imgCanny)
cv2.waitKey(0)

