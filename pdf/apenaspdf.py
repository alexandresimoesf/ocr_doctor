import PyPDF2 as pdf


class PdfReader:

    @staticmethod
    def ler_pdf(arquivo):
        '''
        :param arquivo: Pasta onde estão os arquivos
        :return: Retorna o texto que está no pdf
        '''

        file = open(arquivo, 'rb')


        fileReader = pdf.PdfFileReader(file)


        return fileReader.numPages