from view import View
from model import Model


class Controller:

    def main(self):
        self.visual.main()

    def setar_destino(self, arquivo):
        self.modelo.destino = arquivo
        self.visual.text(self.visual.lblfolderText, self.modelo.destino)
        self.visual.text(self.visual.lblPastaText, self.modelo.contar_arquivos())
        self.visual.allow()

    def iniciar_ocr(self):
        self.visual.forbid()
        for i in self.modelo.arquivosPermitidos:
            self.visual.teste(self.modelo.ler(self.modelo.destino + '/' + i))

    def __init__(self):
        self.visual = View(self)
        self.modelo = Model()


if __name__ == '__main__':
    software = Controller()
    software.main()
