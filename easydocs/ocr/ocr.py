from PIL import Image
import easyocr

def transcribe_image(image):
	image = Image.open(image)
	reader = easyocr.Reader(['en'])
	result = reader.readtext(r'dependencies/lstm_cell.jpg', detail=0)

	return "\n".join(result)

if __name__ == "__main__":
	transcribe_image()
