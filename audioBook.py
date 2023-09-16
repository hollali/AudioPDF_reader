import pyttsx3
import PyPDF2

# Open the PDF file in binary mode
book = open('Your.pdf', 'rb')

# Initialize the PdfFileReader with the PDF file object
pdfReader = PyPDF2.PdfFileReader(book)

# Get the total number of pages in the PDF
pages = pdfReader.numPages

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Loop through the pages starting from page 7
for num in range(6, pages):  # Adjusted range to start from page 7 (0-based index)
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

# Close the PDF file
book.close()
