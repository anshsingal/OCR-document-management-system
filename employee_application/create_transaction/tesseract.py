# import pytesseract
# from PIL import Image
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
convert_image = lambda file:str(((pytesseract.image_to_string(Image.open(file)))))
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def convert(file):
    if file[-3:] == 'pdf':
        text = convert_pdf(file)
    elif file[-3:] == 'jpg' or file[-3:] == 'png' or file[-3:] == 'JPG' or file[-3:] == 'PNG' or file[-4:] == 'JPEG' or file[-3:] == 'bmp':
        text = convert_image(file)
    return text

def convert_pdf(PDF_file):
    pages = convert_from_path(PDF_file, 500)
    image_counter = 1

    for page in pages:
    	filename = "temp_page_"+str(image_counter)+".jpg"
    	page.save(filename, 'JPEG')
    	image_counter = image_counter + 1

    filelimit = image_counter-1

    text = ''
    for i in range(1, filelimit + 1):
        filename = "temp_page_"+str(i)+".jpg"
        text += convert_image(filename)
        text += text.replace('-\n', '')
        os.remove(filename)
    return text

if __name__ == "__main__":
    # print("inside main")
    PDF_file = "C:\\Users\\anshs\\Desktop\\EE_Syllabus.pdf"
    img_file = 'C:\\Users\\anshs\\Desktop\\MAD\\yoyo.png'
    text = convert(PDF_file)
    print(text)
