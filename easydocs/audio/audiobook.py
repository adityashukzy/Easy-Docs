from gtts import gTTS
import pyttsx3
import pdfplumber

def convert_text_to_audio(text_input, save, slow):
	if save:
		audio = gTTS(text=text_input, lang='en', slow=slow)
		audio.save('your_audiobook.mp3')

	elif save == "No":
		speaker = pyttsx3.init()
		speaker.say(text_input)
		speaker.runAndWait()

def convert_pdf_to_audio(pdf_file, slow):
	pdf_text = ''

	try:
		with pdfplumber.open(pdf_file) as pdf:
			page = pdf.pages[0]
			pdf_text += page.extract_text()
		
		audio = gTTS(text=pdf_text, lang='en', slow=slow)
	except:
		return "Not in a readable format."

if __name__ == "__main__":
	sample_text = "This is some test audio to check whether this goddamn thing works!"
	text_to_audio(sample_text, "No", "Yes")
