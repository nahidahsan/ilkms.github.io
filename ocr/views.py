from django.shortcuts import render

# import pytesseract to convert text in image to string
# import pytesseract

# import summarize to summarize the ocred text
# from gensim.summarization.summarizer import summarize
# from .models import MultipleImage
from .forms import ImageUpload
from PIL import Image #Image Processing
import numpy as np #Image Processing 
import os, io
from google.cloud import vision
from google.cloud.vision_v1 import types
import cv2
import ocr 
APP_ROOT = os.path.abspath(ocr.__path__[0])
FILE_path = os.path.join(APP_ROOT,'VisionApi_token.json' )

from django.conf import settings
from .models import Ocr


# Create your views here.
def ocr(request):
    bangla_text = ''
    message = ""
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES) 
        
        if form.is_valid():           
            try:
                form.save()
                
                # image = request.FILES['image']
                # image = image.name
                images = request.FILES.getlist('image')
                pathz = []
                for image in images:
                    image = image.name
                    path = settings.MEDIA_ROOT
                    pathz.append(path + "/images/" + image)
                    Ocr.objects.create(image = image)
                images = Ocr.objects.all()
                print({'images': images})
                # imdir = path + "/images/"
                # images = os.listdir(imdir)
                # images.sort(key = len)
                # images = [cv2.imread(image) for image in images]
   
                os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = FILE_path
                client = vision.ImageAnnotatorClient()
              
                
                
                
                def decode_png(image_data):
                    success, encoded_image = cv2.imencode('.jpg', image_data)
                    content2 = encoded_image.tobytes()
                    return content2 
                
                images = [cv2.imread(path) for path in pathz]
                decode_image = [decode_png(image) for image in images]
                content_image = [types.Image(content = image) for image in decode_image]

                # images = [cv2.imread(path) for path in pathz]
                # decode_image = decode_png(image)
                # content_image = types.Image(content = decode_image)
                
                
                for idx, image in enumerate(content_image):
                    response = client.text_detection(image = image)
                    texts = response.text_annotations 

                # response = client.text_detection(image = content_image)
                # texts = response.text_annotations
                    
                    for text in texts:
                            bangla_text += ('\n"{}"'.format(text.description))
                            break

                
                # os.remove(pathz)
            except:
                message = "check your filename and ensure it doesn't have any space or check if it has any text"

            context = {
                'text': bangla_text,
                # 'summarized_text': summarized_text,
                'message': message
            }
            # print(context)
            return render(request, 'ILKMS_project/OCR_2.html', context)
    # print(context)
    # return render(request, 'formpage.html', context)
    return render(request, 'ILKMS_project/OCR_2.html')
