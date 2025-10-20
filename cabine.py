class CabineStandard:
    def __init__(self, codice, letti, ponte, prezzo):
        self.codice=codice
        self.letti=letti
        self.ponte=ponte
        self.prezzo=prezzo
        self.disponibile=True

    def __str__(self):
        return f"{self.codice} - Prezzo: {self.prezzo}€ - Tipo: {self.__class__.__name__}"

class CabinaDeluxe(CabineStandard):
    def __init__(self, codice, letti, ponte, prezzo, stile):
        super().__init__(codice, letti, ponte, prezzo)
        self.stile=stile


class CabinaAnimali(CabineStandard):
    def __init__(self, codice, letti, ponte, prezzo, numeroAnimali):
        super().__init__(codice, letti, ponte, prezzo)
        self.numeroAnimali=numeroAnimali
