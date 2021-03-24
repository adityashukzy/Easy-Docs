import pandas as pd
import numpy as np
import cv2
import PIL
import json
from PIL import Image
import matplotlib.pyplot as plt
import os
from google.cloud import vision_v1
from google.cloud import vision
import io
from google.cloud.vision_v1 import types
import pathlib

#how do I add the token json file?
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'TokenKeyGCP.json'

client=vision.ImageAnnotatorClient()

#Have to work on document upload too
print('Upload an image: ')

img='pic1.jpg'
imgp=r'C:\Users\Pooja\Documents\ocr_google\stuff'
with io.open(os.path.join(imgp,img),'rb') as fl:
    content=fl.read()

image=vision_v1.types.Image(content=content)

response = client.text_detection(image=image)
text=response.text_annotations

print("Text extracted: ")
l=[]
for i in text:
    l.append(i.description)
print(l[0])

in1=input('Do you want to save this file? Y/N')
if in1=='Y' or in1=='y':
    inp2=input('Enter the desired file name: ')
    with open(inp2,'w+') as file:
        file.write(l[0])
    print('The extracted text has been saved into successfully! :)')
    print('You can now edit your file if required.')
elif in1=='N' or in1=='n':
    print('Thank you for using our Optical Character Recognition functionality.')

else:
    print('Invalid entry.')
