#Importing Libraries
import PyPDF2
import os

file="C:\\Users\\DELL\\OneDrive\\Desktop\\PDSC Workshop\\day2\\2img2pdf\\img2pdf.pdf" #Location of the PDF File
pdf_in_file = open(file,'rb')
inputpdf = PyPDF2.PdfFileReader(pdf_in_file)
pages_no = inputpdf.numPages
output = PyPDF2.PdfFileWriter()

for i in range(pages_no):
    inputpdf = PyPDF2.PdfFileReader(pdf_in_file)
    
    output.addPage(inputpdf.getPage(i))
    output.encrypt('password') #Give your password here
    
    filename=file.replace(".pdf", "")
    protected_location = filename+"_password_protected.pdf"
    with open(protected_location, "wb") as outputStream:
        output.write(outputStream)
    
pdf_in_file.close()

print("Password Protected File Successfully!!")
print("Press 'Y' if you want to delete unprotected file or 'N' if you want to keep previous file.")
choice=input("Do you want to delete previous unprotected file?")
if choice=="Y" or choice=="y":
    os.remove(file)
    print("File Deleted Successfully !!")
elif choice=="N" or choice=="n":
    pass
else:
    print("Your Choice is not valid, both files are still in the same directory, if you want to delete previous file, you can do that manually.")
    pass
