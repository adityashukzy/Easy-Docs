import streamlit as st
from gtts import gTTS
import pysttx3
import PyPDF2

# Summarization Import
from easydocs.summarization.summarize import summarize_url, summarize_doc

# OCR Import
import PIL
from PIL import Image
from google.cloud import vision_v1
from google.cloud import vision
from google.cloud.vision_v1 import types

# Text to Audiobook Import

##########################################################################################

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


def ocr():
	pass

def text_to_audio():
	st.title('PDF-to-audiobook')
	st.subheader('Welcome to the 3rd section of EasyDocs: PDF to audiobook converter')
	st.write('Answer a sequence of questions and upload a file in the specified format so as to obtain an audiobook.')
	st.write('ProTip: To convert an image to a text file, use the OCR functionality provided by EasyDocs :)')

	txt=st.text_area('Paste any text and let EasyDocs do the job for you!')
	#choice=st.radio('Choose the upload format of your document',('Text file','PDF document'))
	in1=st.radio('Do you want to save the output file?',('Yes','No'))
	#if choice=='PDF document':
		#fla=st.file_uploader('Upload a document',type=['pdf'])
		#pdf=PyPDF2.PdfFileReader(fla)

	if in1=='Yes':
		inp=st.radio('Do you want the document to be read in a slower pace?',('Yes','No'))
		if inp=='Yes':
			res1=gTTS(text=txt,lang='en',slow=True)
		elif inp=='No':
		    res1=gTTS(text=txt,lang='en',slow=False)

		res1.save('your_audiobook.mp3')
	#elif choice=='Text file':
		#fla=st.file_uploader('Upload a document',type=['txt'])
		#inp2=('Do you want to save the output file? Y/N')
		#if inp1=='Y' or inp1=='y':
			#res2=gTTS(text=pdf,lang='en',slow=False)
			#res2.save('your_audiobook.mp3')

	elif inp1=='No':
			#numpgs=pdf.numPages
			#for i in range(numpgs):
		        #page=pdf.getPage(i)
		        #content += page.extractText()
	    speaker=pyttsx3.init()
	    speaker.say(txt)
	    speaker.runAndWait()

	#pass

def ezpz():
	pass

# MAIN Function
def main():
	menu = ['Welcome', 'Summarize a URL', 'Summarize a text document', 'Optical Character Recognition', 'Convert text/pdf-to-audiobook', 'Talk to the EzPz bot']
	with st.sidebar.beta_expander("Menu", expanded=False):
		option = st.selectbox('Choose your task', menu)
		st.subheader("Made with ❤️ by Team Agnes")

	if option == 'Welcome':
		# link = ''

		st.title("EasyDocs 📄✍🏼📓 ~ A student friendly ML application")
		st.header('Summarize|Recognize|Revolutionize')
		st.image('data/logo1.jpg', use_column_width=True)
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
		image = st.file_uploader("Upload an image:")

		
		ocr()
	elif option == 'Convert text-to-audiobook':
		text_to_audio()
	elif option == 'Talk to EzPz':
		ezpz()

if __name__ == "__main__":
	main()
