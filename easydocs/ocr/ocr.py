from google.cloud import vision_v1
from google.cloud import vision
from google.cloud.vision_v1 import types
import os
import io
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'dependencies/TokenKeyGCP.json'

def transcribe_image(bytes_image):
	client = vision.ImageAnnotatorClient()

	content = bytes_image
	image = vision_v1.types.Image(content=content)

	response = client.text_detection(image=image)
	text = response.text_annotations
	
	textList = []
	for i in text:
		textList.append(i.description)
	
	transcript = " ".join(textList)

	return transcript

if __name__ == "__main__":
	with io.open("/Users/adityashukla/Documents/GitHub/Easy-Docs/dependencies/logo1.jpg",'rb') as fl:
		content = fl.read()
		transcribeImage(content)
