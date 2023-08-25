import cv2

# Get images from a video 

filename = 'video_name.mp4'

cap = cv2.VideoCapture(filename)

i = 0
while True:
	i+=1
	ret, frame = cap.read()
	if not ret:
		break

	cv2.imshow('frame', frame)
	if i% 15== 0:
		cv2.imwrite(f'frames/{i}_frame.jpg', frame)

	if cv2.waitKey(10) == 27:
		break


cap.release()
cv2.destroyAllWindows()




