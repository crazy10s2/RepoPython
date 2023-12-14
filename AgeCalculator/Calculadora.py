import tkinter as tk
from Pessoa import Pessoa
from datetime import datetime as dt 
from tkinter import messagebox as dt

# Criar o Frame principal

janela = tk.Tk()
janela.geometry('320x320')
janela.title('Age Calculator')
janela.resizable(False, False)
janela.anchor(anchor = 'center')

# Criar Lables
nome = tk.Label(text = 'Nome:', height = 2, font = ('Bookman old style', 14, 'Italic'))
nome.grid(column = 0, row = 2)

ano = tk.Label(text = 'Ano:', height = 2, font = ('Bookman old style', 14, 'Italic'))
ano.grid(column = 0, row = 2)

# Criar Campos (Fields)

campoNome = tk.Entry(width = 12, font = ('Bookman old style', 14))
campoNome.grid(column = 1, row = 2)

campoAno = tk.Entry(width = 12, font = ('Bookman old style', 14))
campoAno.grid(column = 1, row = 2)

# Método calcular

def getInputs():
    try:
       humano = Pessoa(campoNome.get(), int(campoAno.get()))
       limpar()
       mb.showinfo(title = 'Resultado', message = f'Olá {humano.nome}, você tem {humano.idade()} anos de idade.')
    except ValueError:
       mb.showerror(title = 'Erro!', message = 'Informe apenas números no campo  ANO!')

# Método limpar
def limpar() -> None:

    lista = [campoNome, campoAno]
    
    for input in lista:
        input.delete(0, tk.END)
        
# Criar botões

bCalcular = tk.Button(janela, text = 'OK', command = getInputs, width = 10, font = ('Bookman old style', 14))
bCalcular.grid(column = 1, row = 5)
bLimpar = tk.Button(janela, text = 'Limpar', command = limpar, width = 10, font = ('Bookman old style', 14))
bLimpar.grid(column = 0, row = 5)

# Começar a GUI
janela.mainloop()