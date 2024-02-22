import cv2
from flask import Flask,render_template,Response
from imutils.video import WebcamVideoStream

app = Flask(__name__)

print("cv2 version",cv2.__version__)

camera = cv2.VideoCapture(0)
def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
             ret, buffer = cv2.imencode('.jpg', frame)
            # facesdetect=cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
             #gray=cv2.cvtColor(buffer,cv2.COLOR_BGR2GRAY)
             #faces=facesdetect.detectMultiScale(gray,1.3 ,5)
             #for (x,y,w,h) in faces:
              # cv2.rectangle(buffer,(x,y),(x+w,y+h),(50,50,255),2)
               #cv2.imshow("Frame",buffer)
             frame = buffer.tobytes()
             yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/')
def index():

 return render_template("index.html")
 
 
 
@app.route('/video_feed')
def video_feed():
    
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
  
  
  
 #video =cv2.VideoCapture(0)
   #facesdetect=cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
  
   #while True:
  #  ret, frame=video.read()
   # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   # faces=facesdetect.detectMultiScale(gray,1.3 ,5)

  #  for (x,y,w,h) in faces:
  #      cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
  #  cv2.imshow("Frame",frame)
  #  k=cv2.waitKey(1)
   # if k==ord('q'):
   #    break
    
      
   #video.release()
   #cv2.destroyAllWindows()
  #fetch()
   

if __name__=='__main__':
   app.run(debug=True)

  