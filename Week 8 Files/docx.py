#import docx2txt
#my_text = docx2txt.process("D:\sharmila.docx")
#print(my_text)
# creating a pdf file object (object means run time entity)
import PyPDF2
pdfFileObj = open('D:\FilesUnit.pdf', 'rb')
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())
# closing the pdf file object
pdfFileObj.close()
