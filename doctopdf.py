from spire.doc import *
from spire.doc.common import *
from tkinter import filedialog

inputFile = filedialog.askopenfilename()
outputFile = input("Enter file name with extension")

#Create word document
document = Document()
document.LoadFromFile(inputFile)
#Save the document to a PDF file.
document.SaveToFile(outputFile, FileFormat.PDF)
document.Close()
print("Work Done")