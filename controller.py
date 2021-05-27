from viewtk import ViewTk
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
        self.visual.mudar_estado_botao(self.visual.topLevelBtnConectar)
        self.visual.text(self.visual.topLevelVarConectar, arg)

    def top_read_level_variables(self) -> List[Tuple[str, str]]:
        return self.modelo.config_file_get()

    def setar_arquivos_permitidos(self, arquivo):
        self.modelo.arquivos_permitidos(arquivo)

    def setar_destino(self, arquivo):
        if arquivo == '':
            self.visual.message(self.setar_destino, 'Selecione uma pasta')
        elif len(self.modelo.arquivosPermitidosNaLista) > 0:
            self.visual.message(self.setar_destino, 'Você já adicionou os arquivos')
        else:
            self.modelo.destino = arquivo
            self.visual.text(self.visual.lblfolderText, self.modelo.destino)
            self.visual.text(self.visual.lblPastaText, self.modelo.contar_arquivos())
            self.visual.mudar_estado_botao(self.visual.btnOcr, self.visual.checkEditPdf,
                                           self.visual.checkEditJpg, self.visual.checkEditPng,
                                           self.visual.checkEditJpeg, self.visual.checkEditPdfImg)

    def iniciar_ocr(self):
        self.visual.mudar_estado_botao(self.visual.btnOcr, self.visual.checkEditPdf,
                                       self.visual.checkEditJpg, self.visual.checkEditPng,
                                       self.visual.checkEditJpeg, self.visual.checkEditPdfImg)

        if self.modelo.arquivosGuardadosNoContagem == 0:
            self.visual.message(self.iniciar_ocr, 'Não há arquivos adicionados')
        else:
            for i in self.modelo.arquivosPermitidosNaLista:
                self.visual.teste(self.modelo.ler(self.modelo.destino + '/' + i))
            self.modelo.arquivosPermitidosNaLista = []

    def pdf_para_imagem(self):
        self.modelo.pdfParaImagemVar = not self.modelo.pdfParaImagemVar

    def __init__(self, dependence):
        self.modelo = Model()
        self.visual = dependence(self)


if __name__ == '__main__':
    software = Controller(ViewTk)
    software.main()
