import cv2
from flask import Flask,render_template


app = Flask(__name__)

print("cv2 version",cv2.__version__)


#def fetch():
 
  
@app.route('/')
def index():
  
   return render_template('index.html')


if __name__=='__main__':
   app.run(debug=True)

  