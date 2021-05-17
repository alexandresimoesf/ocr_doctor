import PyPDF2 as pdf


class PdfReader:

    @staticmethod
    def ler_pdf(arquivo):
        '''
        :return: Retorna o texto que está no pdf
        '''
        file = open(arquivo, 'rb')

        # creating a pdf reader object
        fileReader = pdf.PdfFileReader(file)

        # return the number of pages in pdf file
        return fileReader.numPages