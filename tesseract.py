from PIL import Image
import pytesseract
import re


def get_pic_text(q_path, a1_path, a2_path, a3_path, nr_path):
    # If you don't have tesseract executable in your PATH, include the following:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

    # Image to string
    q_str   = pytesseract.image_to_string(Image.open(q_path), lang='deu')
    a1_str  = pytesseract.image_to_string(Image.open(a1_path), lang='deu')
    a2_str  = pytesseract.image_to_string(Image.open(a2_path), lang='deu')
    a3_str  = pytesseract.image_to_string(Image.open(a3_path), lang='deu')
    nr_str  = pytesseract.image_to_string(Image.open(nr_path), lang='deu')

    nr_str = re.findall('([0-9]*)', nr_str)
    nr_str = [feld for feld in nr_str if feld != '']
    nr_str = int(nr_str[0])

    q_str = q_str.replace('\n', ' ')
    
    #print(q_str, a1_str, a2_str, a3_str, nr_str)
    return q_str, a1_str, a2_str, a3_str, nr_str

if __name__ == "__main__":
    pass