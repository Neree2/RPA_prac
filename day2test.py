import pytesseract
from docx import Document

def scanEng(img):
    text=pytesseract.image_to_string(img)
    return text

textEng = scanEng('228336.jpg')
print(textEng)