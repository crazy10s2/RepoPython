class Fatorial:
    def _init_(self, num):
        self.num = num

    def calcular_fatorial(self):
        if self.num < 0:
            return
        else:
            fatorial = 1
            for i in range(1, self.num + 1):
                fatorial *= i
            return fatorial