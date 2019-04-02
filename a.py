import textract
text = textract.process('harvard.wav')

print(text)