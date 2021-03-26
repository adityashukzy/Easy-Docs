from gtts import gTTS
import pyttsx3
import pdfplumber

def convert_text_to_audio(text_input, save, slow):
	if save == "Yes":
		if slow == "Yes":
			audio = gTTS(text=text_input, lang='en', slow=True)
		elif slow == "No":
			audio = gTTS(text=text_input, lang='en', slow=False)
		
		audio.save('your_audiobook.mp3')

	elif save == "No":
		speaker = pyttsx3.init()
		speaker.say(text_input)
		speaker.runAndWait()

def convert_pdf_to_audio(pdf_file, save, slow):
	pdf_text = ''

	try:
		with pdfplumber.open(pdf_file) as pdf:
			page = pdf.pages[0]
			pdf_text += page.extract_text()

		print(pdf_text)
		
		if slow == "Yes":
			audio = gTTS(text=pdf_text, lang='en', slow=True)
		elif slow == "No":
			audio = gTTS(text=pdf_text, lang='en', slow=False)
		
		if save == "Yes":
			audio.save('your_audiobook.mp3')
		elif save == "No":
			speaker = pyttsx3.init()
			speaker.say(pdf_text)
			speaker.runAndWait()

	except:
		return "Not in a readable format."

if __name__ == "__main__":
	sample_text = "This is some test audio to check whether this goddamn thing works!"
	convert_text_to_audio(sample_text, "No", "Yes")
