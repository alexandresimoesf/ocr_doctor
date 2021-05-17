import os
from pdf.apenaspdf import PdfReader as Pdf
from imagem.apenasimg import ImgReader as Img
import configparser


class Model:

    @staticmethod
    def config_file_get():
        config = configparser.ConfigParser()
        host = config['mysqlDB']['host'],
        user = config['mysqlDB']['user'],
        passwd = config['mysqlDB']['pass'],
        db = config['mysqlDB']['db']
        return host, user, passwd, db

    @staticmethod
    def config_file_set():
        config = configparser.ConfigParser()
        config.read('config.ini')
        config.set('mysqlDB', 'host', '0.0.0.0')

    @staticmethod
    def ler(arquivo):
        if os.path.splitext(arquivo)[1][1:] == 'pdf':
            return Pdf.ler_pdf(arquivo)
        else:
            return Img.ler_imagem(arquivo)

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
