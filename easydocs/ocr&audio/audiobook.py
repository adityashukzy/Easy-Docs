import numpy as np
from gtts import gTTS
import json
import os
import pyttsx3
import PyPDF2
import streamlit as st

st.title('Hello there!')
st.subheader('A simple text-to-speech converter.')
#pdf='Hey there pooja. how are you?'
inp=st.text_area('Enter text: ')
inp1=st.radio('Do you want to save the output file?',('Yes','No'))
if inp1=='Yes':
    inp2=st.radio('Do you want it read slowly?',('Yes','No'))
    if inp2=='Yes':
        result=gTTS(text=inp,lang='en',slow=True)
    elif inp2=='No':
        result=gTTS(text=inp,lang='en',slow=False)

    result.save('your_audiobook.mp3')

elif inp1=='No':
    #numpgs=pdf.numPages
    #print(numpgs)
    #for i in range(numpgs):
        #page=pdf.getPage(i)
        #content += page.extractText()
    speaker=pyttsx3.init()
    speaker.say(inp)
    speaker.runAndWait()
