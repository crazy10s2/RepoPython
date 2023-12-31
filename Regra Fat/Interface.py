import tkinter as tk
from tkinter.font import Font

class Fatorial:
    def __init__(self, num):
        self.num = num

    def calcular_fatorial(self):
        if self.num < 0:
            return
        else:
            fatorial = 1
            for i in range(1, self.num + 1):
                fatorial *= i
            return fatorial

def calcular():
    num = int(entrada.get())
    f = Fatorial(num)
    resultado["text"] = f.calcular_fatorial()

janela = tk.Tk()
janela.title("Calculadora de Fatorial")
janela.geometry("300x200")
janela.resizable(False, False)

tk.Label(janela, text="Digite um número:", font=Font(family="Bookman Old Style", size=12)).grid(row=0, column=0, padx=5, pady=5)

entrada = tk.Entry(janela)
entrada.grid(row=0, column=1, padx=5, pady=5)

botao = tk.Button(janela, text="Calcular", command=calcular)
botao.grid(row=1, column=0, padx=5, pady=5)

resultado = tk.Label(janela, text="", font=Font(family="Bookman Old Style", size=12))
resultado.grid(row=1, column=1, padx=5, pady=5)

janela.mainloop()
