from gtts import gTTS
import pyttsx3

def convert_to_audio(text_input, save, slow):
	if save:
		audio = gTTS(text=text_input, lang='en', slow=slow)
		audio.save('your_audiobook.mp3')

	elif save == "No":
		speaker = pyttsx3.init()
		speaker.say(text_input)
		speaker.runAndWait()

if __name__ == "__main__":
	sample_text = "This is some test audio to check whether this goddamn thing works!"
	convert_to_audio(sample_text, "No", "Yes")
