import cv2

face_Cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image = cv2.imread('lena.jpg')
imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_Cascade.detectMultiScale(imgGray, 1.1, 4)
image2 = cv2.imread('iron.jpeg')

for (x, y, w, h) in faces:
 image[x:x+w, y:y+h]= cv2.resize(image2, (w,h))

cv2.imshow('img', image)
cv2.waitKey(0)
cv2.destroyAllWindows()