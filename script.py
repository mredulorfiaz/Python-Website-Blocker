import cv2

first_frame = None
video = cv2.VideoCapture(0)

while 1:

	check, frame = video.read()

	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	gray = cv2.GaussianBlur(gray,(25,25),0)

	if first_frame is None:
		first_frame=gray
		continue

	frame_difference = cv2.absdiff(first_frame,gray)

	thresh_delta = cv2.threshold(frame_difference,30,255,cv2.THRESH_BINARY)[1]
	thresh_delta = cv2.dilate(thresh_delta,None, iterations=1)

	(_,contors,_) = cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	for contor in contors:
		if cv2.contourArea(contor) < 1000: #the size depends on what object to capture
			continue

		(x,y,w,h)=cv2.boundingRect(contor)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

	# cv2.imshow("Delta Frame",frame_difference)
	# cv2.imshow("Gray Frame",gray)
	# cv2.imshow("Thresh Frame",thresh_delta)
	cv2.imshow("Motion Detector",frame)

	key =  cv2.waitKey(1)

	if key == ord('q'):
		break

video.release()
cv2.destroyAllWindows()
