import tkinter as tk
from tkinter import Button, Menu, filedialog, Label, StringVar, Toplevel, Entry

E = tk.E
W = tk.W
N = tk.N
S = tk.S
EW = tk.EW


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

        self.db = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='DB', menu=self.db)
        self.db.add_command(label='Config', command=lambda: self.__top_level_db())

    def __top_level_db(self):
        self.topLevelVariables = self.controller.top_read_level_variables()

        self.topLevel = Toplevel()
        self.topLevel.title('DB')
        self.topLevel.geometry('200x150')
        self.topLevel.resizable(False, False)

        self.topLevelVarHost = StringVar()
        self.topLevelVarHost.set(self.topLevelVariables[0:][0])

        self.topLevelVarDb = StringVar()
        self.topLevelVarDb.set(self.topLevelVariables[1:][0])

        self.topLevelVarUser = StringVar()
        self.topLevelVarUser.set(self.topLevelVariables[2:][0])

        self.topLevelVarPass = StringVar()
        self.topLevelVarPass.set(self.topLevelVariables[3:][0])

        self.topLevelVarConectar = StringVar()
        self.topLevelVarConectar.set('...')

        self.topLabelHost = Label(self.topLevel, text='Host :')
        self.topLabelHost.grid(row=0, column=0, pady=4, padx=4, sticky=W)
        self.topEntryHost = Entry(self.topLevel, textvariable=self.topLevelVarHost)
        self.topEntryHost.grid(row=0, column=2, pady=4, padx=4, sticky=W)

        self.topLabelDb = Label(self.topLevel, text='Banco :')
        self.topLabelDb.grid(row=1, column=0, pady=4, padx=4, sticky=W)
        self.topEntryDb = Entry(self.topLevel, textvariable=self.topLevelVarDb)
        self.topEntryDb.grid(row=1, column=2, pady=4, padx=4, sticky=W)

        self.topLabelUser = Label(self.topLevel, text='Usuario :')
        self.topLabelUser.grid(row=2, column=0, pady=4, padx=4, sticky=W)
        self.topEntryUser = Entry(self.topLevel, textvariable=self.topLevelVarUser)
        self.topEntryUser.grid(row=2, column=2, pady=4, padx=4, sticky=W)

        self.topLabelUserPass = Label(self.topLevel, text='Senha :')
        self.topLabelUserPass.grid(row=3, column=0, pady=4, padx=4, sticky=W)
        self.topEntryUserPass = Entry(self.topLevel, textvariable=self.topLevelVarPass)
        self.topEntryUserPass.grid(row=3, column=2, pady=4, padx=4, sticky=W)

        self.topLevelBtnConectar = Button(self.topLevel, text='Conectar', state='disabled', command=lambda: self.controller.top_level_login())
        self.topLevelBtnConectar.grid(row=4, column=0, pady=4, padx=4, sticky=W)
        self.topLabelConectar = Label(self.topLevel, textvariable=self.topLevelVarConectar)
        self.topLabelConectar.grid(row=4, column=2, pady=4, padx=4, sticky=W)

    def text(self, widget, texto):
        widget.set(texto)

    def allow(self):
        self.btnOcr['state'] = 'active'

    def forbid(self):
        self.btnOcr['state'] = 'disabled'

    def teste(self, a):
        print(a.split())

    def main(self):
        self.mainloop()

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.title('Doctor OCR')
        # self.geometry('500x500')
        # self.resizable(False, False)

        self.__menu()
        self.__botoes()
        self.__entradas()
        self.__labels()
