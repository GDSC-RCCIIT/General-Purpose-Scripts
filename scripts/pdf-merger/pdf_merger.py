import os

from PyPDF2 import PdfFileMerger

fnames = []
for fl in os.listdir():
    if fl.endswith(".pdf"):
        fnames.append(fl)

obj = PdfFileMerger()

print("the files that we found are ")
print(*fnames)
print("do you want to order them (y/n)")
n = input()
temp = []
if n == "Y" or n == "y" or n == "yes":
    for i in fnames:
        print(
            "what order do you want for {} enter a number between 1 to {} ".format(
                i, len(fnames)
            )
        )
        ch = int(input())
        temp.append([i, ch])
    temp.sort(key=lambda x: x[1])
    fnames = [i[0] for i in temp]

for fl in fnames:
    obj.append(open(fl, "rb"))

with open("merged.pdf", "wb") as outfile:
    obj.write(outfile)
