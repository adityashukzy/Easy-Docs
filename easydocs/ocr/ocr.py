from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'dependencies\Tesseract-OCR\tesseract.exe'
def ocr_core(image):
	text = pytesseract.image_to_string(image)
	return text

#img = cv2.imread('stuff\pic1.jpg')

def get_grayscale(img):
	return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def remove_noise(img):
	return cv2.medianBlur(img, 5)

def thresholding(img):
	return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def transcribe_image(img):
	img = Image.open(img)

	#img = get_grayscale(img)
	#img = thresholding(img)
	#img = remove_noise(img)

	return (ocr_core(img))
