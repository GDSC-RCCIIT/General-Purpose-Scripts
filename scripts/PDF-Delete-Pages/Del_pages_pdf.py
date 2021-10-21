from PyPDF2 import PdfFileWriter, PdfFileReader
import os

user_path = input("\nEnter the relative/full path of the pdf: ").strip()
path = os.path.normpath(user_path)
pages_del = input("Enter the pages to be deleted separated by a comma: ")

pages_to_delete = pages_del.strip().split(",")
pages_to_delete = [(int(i) - 1) for i in pages_to_delete]

with open(path, "rb") as pdf_file:
    pdf_reader = PdfFileReader(pdf_file)
    num_pages = pdf_reader.numPages

out_of_index_page = []
for num in pages_to_delete:
    if num > num_pages:
        out_of_index_page.append(num)

if len(out_of_index_page) == 0:

    infile = PdfFileReader(path, "rb")
    output = PdfFileWriter()

    for i in range(infile.getNumPages()):
        if i not in pages_to_delete:
            p = infile.getPage(i)
            output.addPage(p)

    inputfile_name = ((path.split("\\")[-1]).split(".pdf"))[0]

    output_name = inputfile_name + "_deleted.pdf"

    with open(output_name, "wb") as f:
        output.write(f)

    print(f"\nThe output pdf is saved as: {output_name}\n")

else:
    print("\nPage number entered is greater than the No of Pages in PDF")
    print("Please Check & Re-Try\n")
