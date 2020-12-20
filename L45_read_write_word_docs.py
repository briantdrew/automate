import os
os.chdir('/Users/btdrew/Downloads')
import docx

# function to get all text in Word doc
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('demo.docx'))