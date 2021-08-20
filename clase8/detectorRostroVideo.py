import cv2
import numpy as np

cap = cv2.VideoCapture('elon_musk_1.mp4') # cargamos el video en vivo

    

faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # Cargamos el clasificador 

while True:
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = faceClassif.detectMultiScale(gray,
                                      scaleFactor=1.3,
                                      minNeighbors=5)

	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)

	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()