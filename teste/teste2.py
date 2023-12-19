from tkinter import *

class RegraDeTres:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular(self):
        return (self.b * self.c) / self.a

root = Tk()
root.title("Regra de Três")
root.geometry("400x300")

a_label = Label(root, text="Valor de A:", font=("Arial", 14))
a_label.pack()
a_entry = Entry(root, width=20, font=("Arial", 14))
a_entry.pack()

b_label = Label(root, text="Valor de B:", font=("Arial", 14))
b_label.pack()
b_entry = Entry(root, width=20, font=("Arial", 14))
b_entry.pack()

c_label = Label(root, text="Valor de C:", font=("Arial", 14))
c_label.pack()
c_entry = Entry(root, width=20, font=("Arial", 14))
c_entry.pack()

def calcular():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    resultado = RegraDeTres(a, b, c).calcular()
    resultado_label.config(text=f"Resultado: {resultado}", font=("Arial", 14))

calcular_button = Button(root, text="Calcular", command=calcular, font=("Arial", 14))
calcular_button.pack()

resultado_label = Label(root, text="", font=("Arial", 14))
resultado_label.pack()

root.mainloop()
