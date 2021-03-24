import streamlit as st

# Summarization Import
from easydocs.summarization.summarize import summarize_url, summarize_doc

# OCR Import


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
	pass

def ezpz():
	pass

# MAIN Function
def main():
	menu = ['Welcome', 'Summarize a URL', 'Summarize a text document', 'Optical Character Recognition', 'Convert text-to-audiobook', 'Talk to EzPz']
	with st.sidebar.beta_expander("Menu", expanded=False):
		option = st.selectbox('Choose your task', menu)
		st.subheader("Made with ❤️ by Team Agnes")

	if option == 'Welcome':
		# link = ''
		# st.image(link, use_column_width=True)

		st.title("EasyDocs 📄✍🏼📓 ~ all your student needs!")
		st.header("EasyDocs is a web-app with the sole purpose of making your life as a student easier!")

	elif option == 'Summarize a URL':
		## URL summarization
		st.title("Summarize URL")
		
		url = st.text_input("URL to summarize", value="https://en.wikipedia.org/wiki/Brad_Pitt")
		sentences_count = st.number_input("Number of sentences in the summary", min_value=5, step=5, key='first')
		
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

			sentences_count = st.number_input("Number of sentences in the summary", min_value=5, step=5, key='second')
			with st.beta_container():
				with st.beta_expander("Find Summary"):
					with st.spinner("Summarizing..."):
						summary = generate_doc_summary(text, sentences_count)
						st.markdown(summary)
		
	elif option ==  'Optical Character Recognition':
		ocr()
	elif option == 'Convert text-to-audiobook':
		text_to_audio()
	elif option == 'Talk to EzPz':
		ezpz()

if __name__ == "__main__":
	main()