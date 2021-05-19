import PyPDF2 as pdf


class PdfReader:

    @staticmethod
    def ler_pdf(arquivo):

        pdf_file = open(arquivo, 'rb')
        read_pdf = pdf.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        return page_content.encode('utf-8')
        # return fileReader.numPages
