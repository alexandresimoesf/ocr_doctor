import tkinter as tk
from tkinter import Button, Menu, filedialog, Label, StringVar, BooleanVar,\
                    Toplevel, Entry, Checkbutton, LabelFrame, messagebox

E = tk.E
W = tk.W
N = tk.N
S = tk.S


class View(tk.Tk):

    def message(self, func, msg):
        self.alert = messagebox.showwarning(func.__name__, msg)

    def __label_frame(self):
        self.labelFramePastaArquivos = LabelFrame(text='Pasta e arquivos')
        self.labelFramePastaArquivos.grid(row=1, column=0, pady=4, padx=4, columnspan=2, sticky=W)

        self.labelFrameCheckButton = LabelFrame(text='Arquivos Permitos')
        self.labelFrameCheckButton.grid(row=2, column=0, pady=4, padx=4, sticky=W)

        self.labelFrameInformacoes = LabelFrame(text='Informações')
        self.labelFrameInformacoes.grid(row=2, column=1, pady=4, padx=4, sticky=W)

    def __labels(self):
        self.lblfolderText = StringVar()
        self.lblfolderText.set('0 arquivos adicionados')
        self.lblAdicionados = Label(self.labelFramePastaArquivos, textvariable=self.lblfolderText)
        self.lblAdicionados.grid(row=1, column=1, pady=4, padx=4, sticky=E)

        self.lblfolder = Label(self.labelFramePastaArquivos, text='Pasta :')
        self.lblfolder.grid(row=1, column=0, pady=4, padx=4)

        self.lblPasta = Label(self.labelFramePastaArquivos, text='Nº de arquivos :')
        self.lblPasta.grid(row=2, column=0, pady=4, padx=4)

        self.lblPastaText = StringVar()
        self.lblPastaText.set('0 arquivos adicionados')
        self.lblPastaC = Label(self.labelFramePastaArquivos, textvariable=self.lblPastaText)
        self.lblPastaC.grid(row=2, column=1, pady=4, padx=4, sticky=W)

        self.lblBanco = Label(self.labelFrameInformacoes, text='Banco: ')
        self.lblBanco.grid(row=0, column=0, pady=4, padx=4, sticky=W)

        self.lblBancoConectadoText = StringVar()
        self.lblBancoConectadoText.set('Não conectado')
        self.lblBancoConectado = Label(self.labelFrameInformacoes, textvariable=self.lblBancoConectadoText)
        self.lblBancoConectado.grid(row=0, column=1, pady=4, padx=4, sticky=W)

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

    def __check_button(self):
        self.checkValuePdf = BooleanVar()
        self.checkValuePdf.set(True)
        self.checkEditPdf = Checkbutton(self.labelFrameCheckButton,
                                        text='PDF',
                                        var=self.checkValuePdf,
                                        command=lambda: self.controller.setar_arquivos_permitidos('pdf')
                                        )
        self.checkEditPdf.grid(row=0, column=0, sticky=W)

        self.checkValueJpg = BooleanVar()
        self.checkValueJpg.set(True)
        self.checkEditJpg = Checkbutton(self.labelFrameCheckButton,
                                        text='JPG',
                                        var=self.checkValueJpg,
                                        command=lambda: self.controller.setar_arquivos_permitidos('jpg')
                                        )
        self.checkEditJpg.grid(row=0, column=1, sticky=W)

        self.checkValueJpeg = BooleanVar()
        self.checkValueJpeg.set(True)
        self.checkEditJpeg = Checkbutton(self.labelFrameCheckButton,
                                         text='JPEG',
                                         var=self.checkValueJpeg,
                                         command=lambda: self.controller.setar_arquivos_permitidos('jpeg')
                                         )
        self.checkEditJpeg.grid(row=1, column=0, sticky=W)

        self.checkValuePng = BooleanVar()
        self.checkValuePng.set(True)
        self.checkEditPng = Checkbutton(self.labelFrameCheckButton,
                                        text='PNG',
                                        var=self.checkValuePng,
                                        command=lambda: self.controller.setar_arquivos_permitidos('png')
                                        )
        self.checkEditPng.grid(row=1, column=1, sticky=W)

    def __top_level_db(self):
        self.topLevelVariables = list(self.controller.top_read_level_variables())

        self.topLevel = Toplevel()
        self.topLevel.title('DB')
        self.topLevel.geometry('200x150')
        self.topLevel.resizable(False, False)

        self.topLevelVarHost = StringVar()
        self.topLevelVarHost.set(self.topLevelVariables[0][1])

        self.topLevelVarDb = StringVar()
        self.topLevelVarDb.set(self.topLevelVariables[1][1])

        self.topLevelVarUser = StringVar()
        self.topLevelVarUser.set(self.topLevelVariables[2][1])

        self.topLevelVarPass = StringVar()
        self.topLevelVarPass.set(self.topLevelVariables[3][1])

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

        self.topLabelPass = Label(self.topLevel, text='Senha :')
        self.topLabelPass.grid(row=3, column=0, pady=4, padx=4, sticky=W)
        self.topEntryPass = Entry(self.topLevel, textvariable=self.topLevelVarPass)
        self.topEntryPass.grid(row=3, column=2, pady=4, padx=4, sticky=W)

        self.topLevelBtnConectar = Button(
            self.topLevel,
            text='Conectar',
            state='active',
            command=lambda: self.controller.top_level_login(
                self.topLevelVarHost.get(),
                self.topLevelVarUser.get(),
                self.topLevelVarPass.get(),
                self.topLevelVarDb.get()
            )
        )
        self.topLevelBtnConectar.grid(row=4, column=0, pady=4, padx=4, sticky=W)
        self.topLabelConectar = Label(self.topLevel, textvariable=self.topLevelVarConectar)
        self.topLabelConectar.grid(row=4, column=2, pady=4, padx=4, sticky=W)

    def text(self, widget, texto):
        widget.set(texto)

    def allow_button(self, widget):
        widget['state'] = 'active'

    def forbid_button(self, widget):
        widget['state'] = 'disabled'

    def teste(self, a):
        print(a.split())

    def main(self):
        self.mainloop()

    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.title('Doctor OCR')
        self.geometry('500x200')
        self.resizable(False, False)

        self.__label_frame()
        self.__menu()
        self.__botoes()
        self.__entradas()
        self.__labels()
        self.__check_button()
