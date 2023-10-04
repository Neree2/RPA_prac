import pytesseract

def scanEng(img):
    text=pytesseract.image_to_string(img)
    return text

textscan=scanEng('chemistry.png')
print(textscan)