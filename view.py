import tkinter as tk
from tkinter import Button, Menu, filedialog, Label, StringVar

E = tk.E
W = tk.W
N = tk.N
S = tk.S


class View(tk.Tk):


    def __labels(self):
        self.lblfolderText = StringVar()
        self.lblfolderText.set('0 arquivos adicionados')
        self.lblAdicionados = Label(self, textvariable=self.lblfolderText)
        self.lblAdicionados.grid(row=1, column=1, pady=4, padx=4, sticky=E)

        self.lblfolder = Label(self, text='Pasta :')
        self.lblfolder.grid(row=1, column=0, pady=4, padx=4)

        self.lblPasta = Label(self, text='Nº de arquivos :')
        self.lblPasta.grid(row=2, column=0, pady=4, padx=4)

        self.lblPastaText = StringVar()
        self.lblPastaText.set('0 arquivos adicionados')
        self.lblPastaC = Label(self, textvariable=self.lblPastaText)
        self.lblPastaC.grid(row=2, column=1, pady=4, padx=4, sticky=W)

    def __entradas(self):
        pass

    def __botoes(self):
        self.btnOcr = Button(self, state='disabled', text="Ler arquivos", command=lambda: self.controller.iniciar_ocr())
        self.btnOcr.grid(row=0, column=0, pady=4, padx=4, sticky=W)

    def __menu(self):
        self.menu = Menu(self, tearoff=0)
        self.config(menu=self.menu)

        self.file = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Arquivo", menu=self.file)
        self.file.add_command(label="Abrir", command=lambda: self.controller.setar_destino(filedialog.askdirectory()))

    def text(self, widget, texto):
        widget.set(texto)

    def allow(self):
        self.btnOcr['state'] = 'active'

    def main(self):
        self.mainloop()

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.title('Doctor OCR')



        self.__menu()
        self.__botoes()
        self.__entradas()
        self.__labels()
