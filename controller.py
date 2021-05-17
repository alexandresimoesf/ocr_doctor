from view import View
from model import Model
from typing import List, Tuple


def top_set_level_variables(func):
    def wrapper(self, *args):
        return func(self, self.modelo.config_file_set(*args))

    return wrapper


class Controller:

    def main(self):
        self.visual.main()

    @top_set_level_variables
    def top_level_login(self, arg):
        self.visual.forbid_button(self.visual.topLevelBtnConectar)
        self.visual.text(self.visual.topLevelVarConectar, arg)

    def top_read_level_variables(self) -> List[Tuple[str, str]]:
        return self.modelo.config_file_get()

    def setar_destino(self, arquivo):
        self.modelo.destino = arquivo
        self.visual.text(self.visual.lblfolderText, self.modelo.destino)
        self.visual.text(self.visual.lblPastaText, self.modelo.contar_arquivos())
        self.visual.allow_button(self.visual.btnOcr)

    def iniciar_ocr(self):
        self.visual.forbid_button(self.visual.btnOcr)
        for i in self.modelo.arquivosPermitidos:
            self.visual.teste(self.modelo.ler(self.modelo.destino + '/' + i))

    def __init__(self):
        self.visual = View(self)
        self.modelo = Model()


if __name__ == '__main__':
    software = Controller()
    software.main()
