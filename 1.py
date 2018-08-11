import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

cascPath = "haarcascade.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

rval, frame = vc.read()

while True:

	if frame is not None:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = faceCascade.detectMultiScale(frame,scaleFactor = 1.1,minNeighbors = 5,minSize=(30 , 30))

		for(x,y,w,h) in faces:
			cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)

	cv2.imshow("preview", frame)
	rval, frame = vc.read()

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

