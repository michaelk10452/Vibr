import os
from google.cloud import vision
from google.cloud.vision_v1 import types
from PIL import Image
from io import BytesIO

#JSON FILE
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vibr-376821-ff0cccac9e6a.json'


# Instantiates a client
client_options = {'api_endpoint': 'eu-vision.googleapis.com'}
client = vision.ImageAnnotatorClient(client_options=client_options)


image = types.Image()
image.source.image_uri = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/2_Chainz_at_Pretty_Girls_Like_Trap_Music_Tour.jpg/1024px-2_Chainz_at_Pretty_Girls_Like_Trap_Music_Tour.jpg'

#### LABEL DETECTION ######
def find_tag(image):
    response_label = client.label_detection(image=image)
    for label in response_label.label_annotations:
        print({'label': label.description, 'score': label.score})


### FACE DETECTION ######

response_face = client.face_detection(image=image)

face_data = []

for face_detection in response_face.face_annotations:
    d = {
        'confidence': face_detection.detection_confidence,
        'joy': face_detection.joy_likelihood,
        'sorrow': face_detection.sorrow_likelihood,
        'surprise': face_detection.surprise_likelihood,
        'anger': face_detection.anger_likelihood
    }
    print(d)


#### IMAGE PROPERTIES ######

response_image = client.image_properties(image=image)

image_data = []

for c in response_image.image_properties_annotation.dominant_colors.colors[:3]:
    d = {
        'color': c.color,
        'score': c.score,
        'pixel_fraction': c.pixel_fraction
    }
    print(d)



#### TEXT DETECTION ######

response_text = client.text_detection(image=image)

for r in response_text.text_annotations:
    d = {
        'text': r.description
    }
    print(d)



def vibr_tags(image_name):
    image = types.Image()
    image.source.image_uri = image_name
    response_label = client.label_detection(image=image)
    for label in response_label.label_annotations:
        if (label.score >= 0.8):
            print("INSIDE THE FUNCTION RN")
            print({'label': label.description, 'score': label.score})
    response_face = client.face_detection(image=image)

    face_data = []

    for face_detection in response_face.face_annotations:
        d = {
            'confidence': face_detection.detection_confidence,
            'joy': face_detection.joy_likelihood,
            'sorrow': face_detection.sorrow_likelihood,
            'surprise': face_detection.surprise_likelihood,
            'anger': face_detection.anger_likelihood
        }
        print(d)




image_name = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/2_Chainz_at_Pretty_Girls_Like_Trap_Music_Tour.jpg/1024px-2_Chainz_at_Pretty_Girls_Like_Trap_Music_Tour.jpg'
vibr_tags(image_name)





