import streamlit as st
import os
from PIL import Image
import numpy as np

from easydocs.summary.summarization import summarize_url, summarize_doc
from easydocs.ocr.ocr import transcribe_image
from easydocs.audio.audiobook import convert_text_to_audio, convert_pdf_to_audio
from easydocs.ezpz.response import load_chatbot, ezpz_bot

## Summarization Functions
def generate_url_summary(url, sentences_count):
	'''
	Generate summary from a provided url and a count of how many sentences should be in the summary.
	'''
	summary = summarize_url(url, sentences_count)
	return summary

def generate_doc_summary(text, sentences_count):
	'''
	Generate summary from a provided url and a count of how many sentences should be in the summary.
	'''
	summary = summarize_doc(text, sentences_count)
	return summary

## Optical Character Recognition
def ocr(image_array):
	transcript = transcribe_image(image_array)
	st.write('Transcribed text: ')
	st.text(transcript)

## Text to Audiobook
def text_to_audio(text_input, slow):
	audio = convert_text_to_audio(text_input, slow)

	audio.save('audiobook.wav')
	st.audio('audiobook.wav', format='audio/wav')
	os.remove('audiobook.wav')

def pdf_to_audio(pdf, slow):
	with st.spinner("Converting PDF to audio... "):
		audio = convert_pdf_to_audio(pdf, slow)
		audio.save('audiobook.wav')

	st.audio('audiobook.wav', format='audio/wav')
	os.remove('audiobook.wav')

## EzPz Chatbot
@st.cache()
def ezpz(textInput):
	model = load_chatbot('dependencies/ezpz_model.h5')
	response = ezpz_bot(model, textInput)
	return response

# MAIN Function
def main():
	menu = ['Welcome', 'Summarize URL', 'Summarize text document', 'Scan image for text (OCR)', 'Read Text Out Loud', 'Convert PDF to audiobook', 'Talk to EzPz!']
	with st.sidebar.beta_expander("Menu", expanded=False):
		option = st.selectbox('Choose your task', menu)
		st.subheader("Made with ❤️ by Team Agnes")

	if option == 'Welcome':
		img_path = "dependencies/black-bg-logo.gif"

		st.image(img_path,width = 500)
		st.subheader("EasyDocs is a web-app with the sole purpose of making your life as a student easier!")

		st.write("*Summarize* long text documents or paragraphs with the click of a button!")
		st.write("Identify, *recognize* and store text obtained from handwritten images or documents!")
		st.write("Explore the extremely convenient method of learning: via *audiobooks*!")
		st.write("Finally, in case you need any help, visit the *Chatbot* section of our application to learn more about EasyDocs.")

	elif option == 'Summarize URL':
		## URL summarization
		st.title("Summarize text from a webpage 🌐")

		st.write("Enter a URL below of any webpage and choose how many sentences long you want the summary to be, give it a moment and enjoy! We recognize the value that a short and crisp summary can have when it comes to skimming through pages and pages of information online and are here to make that experience a little less painful for you!")

		url = st.text_input("URL to summarize", value="https://medium.com/data-science-community-srm/gans-for-the-beginner-f936504732a0")
		sentences_count = st.slider("Number of sentences in the summary: ", min_value=5,step=5,max_value=60,key='first', value=15)

		with st.beta_container():
			with st.beta_expander("Find Summary"):
				with st.spinner("Summarizing..."):
					summary = generate_url_summary(url, sentences_count)
					st.markdown(summary)

	elif option == 'Summarize text document':
		## Document summarization
		st.title("Summarize a text document 📝")
		st.write("Upload a .txt file in the uploader below, wait a second and watch it work its magic! We just made your long document a breeze to read!")

		file = st.file_uploader(label="Upload text file", type=['txt'])
		text = []

		if file is not None:
			for line in file:
				text.append(str(line))

			text = " ".join(text)

			sentences_count = st.slider("Number of sentences in the summary: ", min_value=5,step=5,max_value=30,key='second')
			with st.beta_container():
				with st.beta_expander("Find Summary"):
					with st.spinner("Summarizing..."):
						summary = generate_doc_summary(text, sentences_count)
						st.markdown(summary)

	elif option == 'Scan image for text (OCR)':
		st.title("Transcribe text from an image 🔍")
		st.write("Upload an image of any typed document in the uploader and we'll scan it and give you the text right back! That's it!")

		img_file_buffer = st.file_uploader("Upload an image:",type=['jpg','png'])

		if img_file_buffer is not None:
			image = Image.open(img_file_buffer)
			image_array = np.array(image)
			ocr(image_array)

	elif option ==  'Read Text Out Loud':
		st.title("Read some text out loud 🗣️")
		st.write("Research has routinely shown that humans learn much better when there's an auditory element in addition to just a visual element. Reading long passages of text can be laborious, and especially so for students with learning disorders such as ADHD and Dyslexia. So.... we can read it out to you! And slowly too if you'd prefer 😇")
		text_input = st.text_area('Enter text: ', )

		slow = st.radio("Do you want it read slowly?", ("Yes", "No"))

		if len(text_input) > 0:
			text_to_audio(text_input, slow)

	elif option == 'Convert PDF to audiobook':
		st.title("Convert a PDF to an audiobook 📙")
		st.write("This one goes out to all the audiobook lovers!")
		pdf_file = st.file_uploader("Upload PDF: ", type=['pdf'])

		slow = st.radio("Do you want it read slowly?", ("Yes", "No"))

		if pdf_file is not None:
			pdf_to_audio(pdf_file, slow)

	elif option == 'Talk to EzPz!':
		st.title("EzPz 🤗")
		textInput = st.text_input("You: ", value = "Ask EzPz something about EasyDocs! When you're done, just type exit to leave!")

		if textInput is not "Ask EzPz something about EasyDocs! When you're done, just type exit to leave!":
			resp = ezpz(textInput)
			st.text_area('EzPz: ', value = resp, height = 200)

if __name__ == "__main__":
	main()
