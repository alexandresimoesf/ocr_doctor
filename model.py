import os
from pdf.apenaspdf import PdfReader as Pdf
from imagem.apenasimg import ImgReader as Img

class Model:

    def ler(self, arquivo):
        if os.path.splitext(arquivo)[1][1:] == 'pdf':
            Pdf.ler_pdf(self, arquivo)
        else:
            Img.ler_imagem(self, arquivo)


    def contar_arquivos(self) -> int:
        '''
        :return: Retorna a contagem de todos os arquivos na pasta
        '''
        for i in os.listdir(self.destino):
            if not os.path.splitext(i)[1][1:] in self.extensoesPermitidos:
                continue
            else:
                self.arquivosPermitidos.append(i)
        return len(self.arquivosPermitidos)

    def __init__(self):
        self.arquivosPermitidos: list = []
        self.extensoesPermitidos: list = ['pdf', 'jpg', 'png', 'jpeg']
        self.salvarEm: str = 'C:/Users/Particular/PycharmProjects/ocr/documentos'
        self.destino: str = ''
