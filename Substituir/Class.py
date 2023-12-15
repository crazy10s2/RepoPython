class SubstituirPalavra:
    def __init__(self, palavra_substituir, palavra_substituta):
        self.palavra_substituir = palavra_substituir
        self.palavra_substituta = palavra_substituta

    def substituir(self, frase):
        return frase.replace(self.palavra_substituir, self.palavra_substituta)