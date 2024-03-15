

import os

from google.cloud import vision
from google.cloud.vision_v1 import types
from PIL import Image
from io import BytesIO

def get_google_data(buffer):
    #JSON FILE
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vibr-417223-1e9518f49c43.json'


    # Instantiates a client
    # client_options = {'api_endpoint': 'us-vision.googleapis.com'}
    # client = vision.ImageAnnotatorClient(client_options=client_options)
    client = vision.ImageAnnotatorClient()

    request = {
        'image': {
            'content': buffer
        },
        # 'features': [
        #     {
        #         'type': "L_DETECTION",
        #         'maxResults': 5
        #     }
        # ]
    }

    # request = {
    #     "requests":[
    #     {
    #         "image":{
    #             'content' : buffer
    #     },
    #     "features":[
    #         {
    #             "type":"LABEL_DETECTION",
    #             "maxResults":5
    #         }
    #     ]
    #     }
    #     ]
    # }

    response = client.annotate_image(request)
    # print(response.label_annotations)
    data=vision.AnnotateImageResponse.to_dict(response)["label_annotations"]
    my_string = ""
    for i in range (min(len(data),5)):
        my_string += (data[i]['description'] +",")
        
    return my_string

    # print(data)
    # for label in data['labelAnnotations']:
    #     my_string+=(label.description+',')
    #     i=i+1



    # image = types.Image()
    # image.source.image_uri = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/2_Chainz_at_Pretty_Girls_Like_Trap_Music_Tour.jpg/1024px-2_Chainz_at_Pretty_Girls_Like_Trap_Music_Tour.jpg'



    #### LABEL DETECTION ######
    
    # response_label = client.label_detection(image=image)
    # my_string=""
    # i=0
    # for label in response_label.label_annotations:
    #     my_string+=(label.description+',')
    #     i=i+1
        # print({'label': label.description, 'score': label.score})
    # print(my_string)
    # try:


        #### FACE DETECTION ######

        # response_face = client.face_detection(image=image)

        # face_data = []

        # for face_detection in response_face.face_annotations:
        #     d = {
        #         'confidence': face_detection.detection_confidence,
        #         'joy': face_detection.joy_likelihood,
        #         'sorrow': face_detection.sorrow_likelihood,
        #         'surprise': face_detection.surprise_likelihood,
        #         'anger': face_detection.anger_likelihood
        #     }
        #     print(d)



        #### IMAGE PROPERTIES ######

#         response_image = client.image_properties(image=image)

#         image_data = []

#         for c in response_image.image_properties_annotation.dominant_colors.colors[:3]:
#             d = {
#                 'color': c.color,
#                 'score': c.score,
#                 'pixel_fraction': c.pixel_fraction
#             }
#             print(d)



#         #### TEXT DETECTION ######

#         response_text = client.text_detection(image=image)

#         for r in response_text.text_annotations:
#             d = {
#                 'text': r.description
#             }
#             print(d)

#     except :
#         return(my_string)
# print(get_google_data())

