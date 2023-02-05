from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from PIL import Image
from io import BytesIO
from google.cloud import vision
from google.cloud.vision_v1 import types
from io import BytesIO
import os

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vibr-376821-ff0cccac9e6a.json'


# Instantiates a client
# client_options = {'api_endpoint': 'eu-vision.googleapis.com'}
# client = vision.ImageAnnotatorClient(client_options=client_options)

counter=0
app = Flask(__name__)

@app.route('/')
def home():
   return "hello 3"
	
@app.route('/upload', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      image=request.files['file']
      img = Image.open(image)  # load with Pillow
      print(img.size)          # show image size (width, height)
      global counter
      img.save('staticFiles/image'+str(counter)+'.png')   # save it
      counter=counter+1 
      buffer=BytesIO()
      img.save(buffer,format="PNG")
      my_vision_image=buffer.getvalue()
      print(my_vision_image)
      return 'file uploaded successfully'
	
if __name__ == '__main__':
   app.run(debug = True)