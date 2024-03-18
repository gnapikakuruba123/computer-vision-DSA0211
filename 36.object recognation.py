import cv2

# Load the watch cascade classifier
watch_cascade = cv2.CascadeClassifier(r"C:\Users\SRAVAN\Downloads\cute-things.xml")

# Check if the classifier was loaded successfully
if watch_cascade.empty():
    print("Error: Unable to load cascade classifier.")
    exit()
else:
    print("Cascade classifier loaded successfully.")

# Continue with the rest of your code
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
watches = watch_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
for (x, y, w, h) in watches:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('Watches Detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
