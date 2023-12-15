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
        master.geometry("400x300")
        master.resizable(width=False, height=False)

        self.label = Label(master, text="Digite a palavra a ser substituída:", font=("Arial", 12))
        self.label.pack(anchor="center")

        self.entry1 = Entry(master, font=("Arial", 12))
        self.entry1.pack()

        self.label2 = Label(master, text="Digite a palavra substituta:", font=("Arial", 12))
        self.label2.pack()

        self.entry2 = Entry(master, font=("Arial", 12))
        self.entry2.pack()

        self.label3 = Label(master, text="Digite a frase:", font=("Arial", 12))
        self.label3.pack()

        self.entry3 = Entry(master, font=("Arial", 12))
        self.entry3.pack()

        self.button = Button(master, text="Substituir", command=self.substituir_palavra, font=("Arial", 12))
        self.button.pack()

        self.result_label = Label(master, text="", font=("Arial", 12))
        self.result_label.pack()

    def substituir_palavra(self):
        palavra_substituir = self.entry1.get()
        palavra_substituta = self.entry2.get()
        frase = self.entry3.get()

        substituidor = SubstituirPalavra(palavra_substituir, palavra_substituta)
        resultado = substituidor.substituir(frase)

        self.result_label.config(text=resultado, font=("Arial", 12))

root = Tk()
my_gui = SubstituirPalavraInterface(root)
root.mainloop()