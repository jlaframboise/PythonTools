import PyPDF2

path1 = 'JacPdf.pdf'
path2 = 'LiaPdf.pdf'
outPath = 'Result.pdf'

def combinePdf(path1, path2, outPath):


    pdf1 = open(path1, 'rb')
    pdf2 = open(path2, 'rb')

    pdfReader1 = PyPDF2.PdfFileReader(pdf1)
    pdfReader2 = PyPDF2.PdfFileReader(pdf2)

    pdfWriter = PyPDF2.PdfFileWriter()

    for page in range(pdfReader1.numPages):
        pdfWriter.addPage(pdfReader1.getPage(page))
    for page in range(pdfReader2.numPages):
        pdfWriter.addPage(pdfReader2.getPage(page))

    pdfOutFile = open(outPath, 'wb')
    pdfWriter.write(pdfOutFile)
    pdfOutFile.close()
    pdf1.close()
    pdf2.close()


combinePdf(path1, path2, outPath)