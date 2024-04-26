import pyttsx3, PyPDF2
from PyPDF2 import PdfReader

pdfreader = PyPDF2.PdfReader(open('The_Ants_and_The_Pen.pdf','rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n',' ')
    print(clean_text)

speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()
