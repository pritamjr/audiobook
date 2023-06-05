import pyttsx3
import PyPDF2

book = open('oop.pdf','rb')
pdfRead = PyPDF2.PdfReader(book)
pages = len(pdfRead.pages)

speaker = pyttsx3.init()
page_number = 7  # Replace with the desired page number
page = pdfRead.pages[page_number]
text = page.extract_text()
speaker.say(text)
speaker.runAndWait()