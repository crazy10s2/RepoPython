import tkinter as tk

def inverter_string():
    texto = entrada.get()
    texto_invertido = texto[::-1]
    resultado.config(text=texto_invertido)

janela = tk.Tk()
janela.title("Inversor de String")
janela.geometry("300x200")
janela.resizable(False, False)
janela.anchor("center")

entrada = tk.Entry(janela, width=30)
entrada.pack(pady=10)

botao = tk.Button(janela, text="Inverter", command=inverter_string)
botao.pack(pady=5)

resultado = tk.Label(janela, text="")
resultado.pack(pady=10)
janela.mainloop()
