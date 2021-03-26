import streamlit as st

from easydocs.summarization import summarize_url, summarize_doc
from easydocs.ocr import transcribe_image
from easydocs.audiobook import convert_text_to_audio, convert_pdf_to_audio

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
def ocr(bytes_image):
	transcript = transcribe_image(bytes_image)
	st.subheader(transcript)

## Text to Audiobook
def text_to_audio(text_input, save, slow):
	if save == "Yes":
		save = True
	elif save == "No":
		save = False
	
	if slow == "Yes":
		slow = True
	elif slow == "No":
		slow = False

	convert_text_to_audio(text_input, save, slow)

def pdf_to_audio(pdf, slow):
	if slow == "Yes":
		slow = True
	elif slow == "No":
		slow = False

	convert_pdf_to_audio(pdf, slow)

## EzPz Chatbot
def ezpz():
	pass

# MAIN Function
def main():
	menu = ['Welcome', 'Summarize a URL', 'Summarize a text document', 'Optical Character Recognition', 'Text-to-audiobook', 'PDF-to-audiobook', 'Talk to the EzPz bot']
	with st.sidebar.beta_expander("Menu", expanded=False):
		option = st.selectbox('Choose your task', menu)
		st.subheader("Made with ❤️ by Team Agnes")

	if option == 'Welcome':
		img_path = "dependencies/logo.png"

		st.image(img_path, use_column_width=True)
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
		img_file_buffer = st.file_uploader("Upload an image:")

		if img_file_buffer is not None:
			bytes_image = img_file_buffer.getvalue()
			ocr(bytes_image)

	elif option == 'Text-to-audiobook':
		st.title('Hello there!')
		st.subheader('A simple text-to-speech converter.')
		text_input = st.text_area('Enter text: ')
		
		save = st.radio('Do you want to save the output file?', ("Yes", "No"))
		slow = st.radio("Do you want it read slowly?", ("Yes", "No"))
		text_to_audio(text_input, save, slow)

	elif option == "PDF-to-audiobook":
		pdf_file = st.file_uploader("Upload PDF: ", type=['pdf'])
		slow = st.radio("Do you want it read slowly?", ("Yes", "No"))

		pdf_to_audio(pdf_file, slow)

	elif option == 'Talk to EzPz':
		ezpz()

if __name__ == "__main__":
	main()
