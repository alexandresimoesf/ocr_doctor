import os
from pdf.apenaspdf import PdfReader as Pdf
from imagem.apenasimg import ImgReader as Img
import configparser


class Model:

    @staticmethod
    def config_file_get():
        config = configparser.ConfigParser()
        config.read('config.ini')
        host = config['dbDoctor']['host'],
        user = config['dbDoctor']['user'],
        passwd = config['dbDoctor']['password'],
        db = config['dbDoctor']['db']
        return host, db, user, passwd

    @staticmethod
    def config_file_set():
        config = configparser.ConfigParser()
        config.read('config.ini')
        config.set('dbDoctor', 'host', '0.0.0.0')
        config.set('dbDoctor', 'user', '0.0.0.0')
        config.set('dbDoctor', 'password', '0.0.0.0')
        config.set('dbDoctor', 'db', '0.0.0.0')

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
