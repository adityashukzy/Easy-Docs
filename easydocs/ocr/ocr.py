from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'Easy-Docs\dependencies\Tesseract-OCR\tesseract.exe'
def ocr_core(image):
	text = pytesseract.image_to_string(image)
	return text

#img = cv2.imread('stuff\pic1.jpg')

def transcribe_image(img):
	img = Image.open(img)

	return (ocr_core(img))
