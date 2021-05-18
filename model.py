import os
from typing import List, Tuple
import configparser

from pdf.apenaspdf import PdfReader as Pdf
from imagem.apenasimg import ImgReader as Img
from base.facade import Repository


class Model:

    @staticmethod
    def config_file_get() -> List[Tuple[str, str]]:
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config.items('dbDoctor')

    @staticmethod
    def config_file_set(*args):
        config = configparser.ConfigParser()
        config.read('config.ini')
        config.set('dbDoctor', 'host', args[0:][0])
        config.set('dbDoctor', 'user', args[1:][0])
        config.set('dbDoctor', 'password', args[2:][0])
        config.set('dbDoctor', 'db', args[3:][0])
        with open(r'config.ini', 'w') as configfile:
            config.write(configfile)
        configfile.close()
        return 'Falta implementar DB'

    @staticmethod
    def ler(arquivo) -> List:
        if os.path.splitext(arquivo)[1][1:] == 'pdf':
            return Pdf.ler_pdf(arquivo)
        else:
            return Img.ler_imagem(arquivo)

    def login_bd_postgres(self):
        pass

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

    def arquivos_permitidos(self, arquivo):
        if arquivo in self.extensoesPermitidos:
            self.extensoesPermitidos.remove(arquivo)
        else:
            self.extensoesPermitidos.append(arquivo)

    def __init__(self):
        self.arquivosPermitidos: list = []
        self.extensoesPermitidos: list = ['pdf', 'jpg', 'png', 'jpeg']
        self.salvarEm: str = 'C:/Users/Particular/PycharmProjects/ocr/documentos'
        self.destino: str = ''
