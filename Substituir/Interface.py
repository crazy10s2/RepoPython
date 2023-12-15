from tkinter import *

class SubstituirPalavra:
    def __init__(self, palavra_substituir, palavra_substituta):
        self.palavra_substituir = palavra_substituir
        self.palavra_substituta = palavra_substituta

    def substituir(self, frase):
        return frase.replace(self.palavra_substituir, self.palavra_substituta)

class SubstituirPalavraInterface:
    def __init__(self, master):
        self.master = master
        master.title("Substituir Palavra")

        self.label = Label(master, text="Digite a palavra a ser substituída:")
        self.label.pack()

        self.entry1 = Entry(master)
        self.entry1.pack()

        self.label2 = Label(master, text="Digite a palavra substituta:")
        self.label2.pack()

        self.entry2 = Entry(master)
        self.entry2.pack()

        self.label3 = Label(master, text="Digite a frase:")
        self.label3.pack()

        self.entry3 = Entry(master)
        self.entry3.pack()

        self.button = Button(master, text="Substituir", command=self.substituir_palavra)
        self.button.pack()

        self.result_label = Label(master, text="")
        self.result_label.pack()

    def substituir_palavra(self):
        palavra_substituir = self.entry1.get()
        palavra_substituta = self.entry2.get()
        frase = self.entry3.get()

        substituidor = SubstituirPalavra(palavra_substituir, palavra_substituta)
        resultado = substituidor.substituir(frase)

        self.result_label.config(text=resultado)

root = Tk()
my_gui = SubstituirPalavraInterface(root)
root.mainloop()