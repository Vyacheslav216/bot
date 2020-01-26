import cv2
import os
def recognize(path):

	image_path = path
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	image = cv2.imread(image_path)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor= 1.2,
    minNeighbors= 5,
    minSize=(10, 10)

	)
	faces_detected =format(len(faces))

	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255),3)
	if(int(faces_detected)>0):
		cv2.imwrite(path, image)
	else:
		os.remove(path)
	return faces_detected
