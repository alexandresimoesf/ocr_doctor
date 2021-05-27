from abc import ABC, abstractmethod

class View(ABC):

    @abstractmethod
    def message(self, func, msg):
        pass

    @abstractmethod
    def label_frame(self):
        pass

    @abstractmethod
    def labels(self):
        pass

    @abstractmethod
    def entradas(self):
        pass

    @abstractmethod
    def botoes(self):
        pass

    @abstractmethod
    def menu(self):
        pass

    @abstractmethod
    def check_button(self):
        pass

    @abstractmethod
    def top_level_db(self):
        pass

    @abstractmethod
    def text(self, widget, texto):
        pass

    @abstractmethod
    def teste(self, a):
        pass

    @abstractmethod
    def main(self):
        pass

    def __init__(self, controller):
        self.controller = controller

