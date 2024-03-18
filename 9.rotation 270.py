import cv2

# Path to the image
path = r"C:\Users\SRAVAN\Downloads\image.jpeg"

# Read the image
src = cv2.imread(path)

# Rotate the image by 270 degrees counterclockwise
rotated_image = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)

# Display the rotated image
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
