import pytesseract
import cv2

def detect_storm(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang='por')
    return "tempestade" in text.lower()
