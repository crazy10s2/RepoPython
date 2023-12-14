class InversorDeString:
    def __init__(self, texto):
        self.texto = texto

    def inverter(self):
        return self.texto[::-1]

texto = input("Digite uma string: ")
inversor = InversorDeString(texto)
print(inversor.inverter())
