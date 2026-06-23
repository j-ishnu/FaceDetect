import cv2
#opens haarscade
face_cascade=cv2.CascadeClassifier(
	"haarcascade_frontalface_default.xml"
)
cam=cv2.VideoCapture(0)
ret,frame=cam.read()
#converts to gray
gray=cv2.cvtColor(
	frame,cv2.COLOR_BGR2GRAY
)
#detect face from gray
faces=face_cascade.detectMultiScale(
	gray
)
#draws rectangle on detected face
for x,y,w,h in faces:
	cv2.rectangle(
		frame,
		(x,y),
		(x+w,y+h),
		(0,255,0),
		3
	)
#prints the face with rectangle
cv2.imshow("image",frame)
cv2.waitKey(0)	
