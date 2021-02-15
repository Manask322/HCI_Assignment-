import textract


text = textract.process('harvard.wav')
#This prints the text
print(text)
