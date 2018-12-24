import cv2
import pytesseract


imPath = './res/OCR-chinese.png'

# Uncomment the line below to provide path to tesseract manually
# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Define config parameters.
# '-l eng'  for using the English language
# '--oem 1' for using LSTM OCR Engine
config = ('-l chi_sim --oem 1 --psm 3')

# Read image from disk
im = cv2.imread(imPath, cv2.IMREAD_COLOR)

# Run tesseract OCR on image
text = pytesseract.image_to_string(im, config=config)

# Print recognized text
print(text)