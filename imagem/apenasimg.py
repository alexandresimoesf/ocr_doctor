import numpy as np
import cv2
import pytesseract as ocr

try:
    from PIL import Image
except ImportError:
    import Image


class ImgReader:
    ocr.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    @staticmethod
    def ler_imagem(arquivo):
        '''
        :param filename: Pasta onde estão os arquivos
        :return: Retorna o texto que está na imagem com tratamento
        '''

        imagem = Image.open(arquivo).convert('RGB')

        # convertendo em um array editável de numpy[x, y, CANALS]
        npimagem = np.asarray(imagem).astype(np.uint8)

        # diminuição dos ruidos antes da binarização
        npimagem[:, :, 0] = 0  # zerando o canal R (RED)
        npimagem[:, :, 2] = 0  # zerando o canal B (BLUE)

        # atribuição em escala de cinza
        im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY)

        # aplicação da truncagem binária para a intensidade
        # pixels de intensidade de cor abaixo de 127 serão convertidos para 0 (PRETO)
        # pixels de intensidade de cor acima de 127 serão convertidos para 255 (BRANCO)
        # A atrubição do THRESH_OTSU incrementa uma análise inteligente dos nivels de truncagem
        ret, thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # reconvertendo o retorno do threshold em um objeto do tipo PIL.Image
        binimagem = Image.fromarray(thresh)

        # chamada ao tesseract OCR por meio de seu wrapper
        phrase = ocr.image_to_string(binimagem)

        # impressão do resultado
        return phrase
