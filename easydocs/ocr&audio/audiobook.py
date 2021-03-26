import numpy as np
from gtts import gTTS
import json
import os
import pyttsx3
#import PyPDF2
import streamlit as st
import pdfplumber

st.title('Hello there!')
st.subheader('A simple text-to-speech converter.')
ch=st.radio('Options to upload text:',('A PDF','Text input'))
if ch=='A PDF':
    pdf1=st.file_uploader('Upload a pdf file',type=['pdf'])
    #pdf2 = str(pdf1.read(),"utf-8")
    #pdf_reader=PyPDF2.PdfFileReader(pdf2)
    #numpgs=pdf.numPages
    #print(numpgs)
    content=''
    #for i in range(numpgs):
        #page=pdf_reader.getPage(i)
        #content += page.extractText()
    try:
        with pdfplumber.open(pdf1) as pdf2:
            page=pdf2.pages[0]
            content+=page.extract_text()
        st.write(content)
    except:
        st.write('Not in a readable format.')

elif ch=='Text input':
    content=st.text_area('Enter text: ')

inp1=st.radio('Do you want to save the output file?',('Yes','No'))
if inp1=='Yes':
    inp2=st.radio('Do you want it read slowly?',('Yes','No'))
    if inp2=='Yes':
        result=gTTS(text=content,lang='en',slow=True)
    elif inp2=='No':
        result=gTTS(text=content,lang='en',slow=False)

    result.save('your_audiobook.mp3')

elif inp1=='No':

    speaker=pyttsx3.init()
    speaker.say(content)
    speaker.runAndWait()
