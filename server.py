from flask import Flask, render_template, request
# from werkzeug.utils import secure_filename
# from werkzeug.datastructures import  FileStorage
from PIL import Image
from io import BytesIO
# from google.cloud import vision
# from google.cloud.vision_v1 import types
from io import BytesIO
# import os
from spotifyAPI import spotify_API_call
from vibr_google_vision_api import get_google_data
from flask_cors import CORS
# from flask import render_template
import json
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vibr-376821-ff0cccac9e6a.json'


# Instantiates a client
# client_options = {'api_endpoint': 'eu-vision.googleapis.com'}
# client = vision.ImageAnnotatorClient(client_options=client_options)

counter=0
app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
@app.route('/')
def home():
   fp=open("index.html","r")
   data=fp.read()
   fp.close()
   return data
	
@app.route('/main.js')
def main():
   fp=open("main.js","r")
   data=fp.read()
   fp.close()
   return data

@app.route('/upload', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      image=request.files['file']
      img = Image.open(image)  # load with Pillow
      print(img.size)          # show image size (width, height) 
      buffer=BytesIO()
      img.save(buffer,format="PNG")
      b64img = buffer.getvalue()
      print(spotify_API_call(get_google_data(b64img)))
      return json.dumps(spotify_API_call(get_google_data(b64img)))
	
if __name__ == '__main__':
   app.run(debug = True)