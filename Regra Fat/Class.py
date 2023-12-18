class CurrencyConverter:
    def __init__(self):
        self.usd_rate = 5.50

    def convert(self, real):
        return real / self.usd_rate

converter = CurrencyConverter()
real = 100
dollar = converter.convert(real)
print(f"{real:.2f} Reais equivalem a {dollar:.2f} Dólares.")
