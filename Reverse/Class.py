class InversorDeString:
    def __init__(self, string):
        self.string = string

    def inverter(self):
        return self.string[::-1]

string = input("Digite uma string: ")
inversor = InversorDeString(string)
print(f"A string invertida é: {inversor.inverter()}")
