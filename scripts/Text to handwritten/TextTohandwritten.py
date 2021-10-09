import pywhatkit

text = input("Enter the text which you want to convert into handwritten: \n")

pywhatkit.text_to_handwriting(text,rgb=[0,0,0])
