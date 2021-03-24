import numpy as np
from gtts import gTTS
import json
import os
import pyttsx3
import PyPDF2

print('Welcome to the 3rd section of the app: PDF to audiobook converter')
print('Upload any pdf file:')
print('ProTip: To convert an image to a text file, use the OCR functionality provided by EasyDocs :)')

#Have to add functionality to accept either pdf or txt file
#path=r'C:/Users/Pooja/Documents/ocr_google/stuff/oops_pdfe.pdf'

with open(path,'rb') as fla:
    pdf=PyPDF2.PdfFileReader(fla)

inp=input('Do you want it to be read in a slower pace? Y/N')
if inp=='Y':
    result=gTTS(text=pdf,lang='en',slow=True)
elif inp=='N':
    result=gTTS(text=pdf,lang='en',slow=False)
else:
    print('Enter only Y/N for yes or no.')

inp1=input('Do you want to save the output file? Y/N')
if inp1=='Y' or inp1=='y':
    result.save('your_audiobook.mp3')

elif inp1=='N' or inp1=='n':
    page=pdf.getPage(1)
    content=pdf.extractText(page)
    speaker=pyttsx3.init()
    speaker.say(content)
    speaker.runAndWait()

else:
    print('Invalid entry :(')
