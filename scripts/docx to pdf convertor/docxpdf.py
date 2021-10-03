import os
from docx2pdf import convert

#convert("word_images.docx", "C:/python/python-docx-to-pdf/word_images.pdf")

#convert("word_images2.docx", "C:/python/python-docx-to-pdf/word_images2.pdf")

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
	fbasename = os.path.splitext(os.path.basename(f))[0]
	if f.endswith('.docx'):
		convert(f, os.path.realpath('.') + '/' + fbasename + '.pdf')