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
def ezpz(textInput):
	model = load_chatbot('dependencies/ezpz_model.h5')
	response = ezpz_bot(model, textInput)
	return response

# MAIN Function
def main():
	menu = ['Welcome', 'Summarize a URL', 'Summarize a text document', 'Optical Character Recognition', 'Text-to-audiobook', 'PDF-to-audiobook', 'Talk to EzPz']
	with st.sidebar.beta_expander("Menu", expanded=False):
		option = st.selectbox('Choose your task', menu)
		st.subheader("Made with ❤️ by Team Agnes")

	if option == 'Welcome':
		img_path = "dependencies/logo_transparent.png"

		st.image(img_path, width = 500)
		st.title("EasyDocs 📄✍🏼📓 ~ A student friendly ML application")

		st.subheader("EasyDocs is a web-app with the sole purpose of making your life as a student easier!")

		st.write("*Summarize* long text documents or paragraphs with the click of a button!")
		st.write("Identify, *recognize* and store text obtained from handwritten images or documents!")
		st.write("Explore the extremely convenient method of learning: via *audiobooks*!")
		st.write("Finally, in case you need any help, visit the *Chatbot* section of our application to learn more about EasyDocs.")

	elif option == 'Summarize a URL':
		## URL summarization
		st.title("Summarize URL")

		url = st.text_input("URL to summarize", value="https://en.wikipedia.org/wiki/Brad_Pitt")
		sentences_count = st.slider("Number of sentences in the summary: ", min_value=5,step=5,max_value=30,key='first')

		with st.beta_container():
			with st.beta_expander("Find Summary"):
				with st.spinner("Summarizing..."):
					summary = generate_url_summary(url, sentences_count)
					st.markdown(summary)

	elif option == 'Summarize a text document':
		## Document summarization
		st.title("Summarize a text document")
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

	elif option ==  'Optical Character Recognition':
		st.title("Transcribe text from an image")
		img_file_buffer = st.file_uploader("Upload an image:",type=['jpg','png'])

		if img_file_buffer is not None:
			image = Image.open(img_file_buffer)
			image_array = np.array(image)
			ocr(image_array)

	elif option == 'Text-to-audiobook':
		st.title('Hello there!')
		st.subheader('A simple text-to-speech converter.')
		text_input = st.text_area('Enter text: ')

		# save = st.radio('Do you want to save the output file?', ("Yes", "No"))
		slow = st.radio("Do you want it read slowly?", ("Yes", "No"))

		if len(text_input) > 0:
			text_to_audio(text_input, slow)

	elif option == "PDF-to-audiobook":
		st.title("Convert a PDF to an audiobook")
		st.subheader("Once the file is ready, you can play it here or right-click and download!")
		pdf_file = st.file_uploader("Upload PDF: ", type=['pdf'])
		# save = st.radio('Do you want to save the output file?', ("Yes", "No"))
		slow = st.radio("Do you want it read slowly?", ("Yes", "No"))

		if pdf_file is not None:
			pdf_to_audio(pdf_file, slow)

	elif option == 'Talk to EzPz':
		st.title("EzPz ~ The Chatbot")
		textInput = st.text_input("You: ", value = "Ask EzPz something about EasyDocs! When you're done, just type exit to leave!")

		resp,tg=ezpz(textInput)
		st.write(tg)
		st.text_area('EzPz: ',value=resp,height=200)

if __name__ == "__main__":
	main()
