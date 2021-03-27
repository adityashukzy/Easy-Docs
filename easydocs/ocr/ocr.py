from PIL import Image
import easyocr

def transcribe_image(image_array):
	reader = easyocr.Reader(['en'])
	result = reader.readtext(image_array, detail=0)

	return "\n".join(result)

if __name__ == "__main__":
	transcribe_image(r'dependencies/lstm_cell.jpg')
