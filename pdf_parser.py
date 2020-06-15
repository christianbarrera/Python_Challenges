import PyPDF2
import re

# Reads in a PDF and uses regex to locate desired strings. 
pdfFile = "my_bill.pdf"
pdfRead = PyPDF2.PdfFileReader(pdfFile)

# iterate through all pages to look for the word "Electric"
for i in range(0, pdfRead.getNumPages()):
	if "Electric" in pdfRead.getPage(i).extractText()[:1000]:
		print("works")
		pageContent = pdfRead.getPage(i).extractText()
		break
	else:
		print("NEXT")


Meter_number = re.findall(r"Meter Number: [0-9]{8}", pageContent)[0][-8:]
taxes = re.findall(r"Total Taxes & Fees on Electric Charges  \n(-?\s*\$[0-9]*.?[0-9]{2})", pageContent)[0]
print("Meter number:", Meter_number.replace(" ", ""))
print("Electric Tax total amount:", taxes.replace(" ", ""))

