import cv2

video =cv2.VideoCapture(0)
facesdetect=cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
while True:
    ret,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=facesdetect.detectMultiScale(gray,1.3 ,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
       break  

video.release()
cv2.destroyAllWindows()