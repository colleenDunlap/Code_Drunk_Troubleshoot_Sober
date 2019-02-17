import PyPDF2
import unicodedata
#pdf import code from https://www.geeksforgeeks.org/working-with-pdf-files-in-python/

#file Object
pdfFileObj = open('samplePDFMultiPage.pdf', 'rb')
#reader Object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
numPages = pdfReader.numPages
#page Object
for iPage in range(0,numPages):
	pageObj = pdfReader.getPage(iPage)
	text = pageObj.extractText()
	string = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
	print(string);

pdfFileObj.close()
