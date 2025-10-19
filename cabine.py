class CabineStandard:
    def __init__(self, codice, letti, ponte, prezzo):
        self.codice=codice
        self.letti=letti
        self.ponte=ponte
        self.prezzo=prezzo
        self.disponibile=True


class CabinaDeluxe(CabineStandard):
    def __init__(self, codice, letti, ponte, prezzo, stile):
        super().__init__(codice, letti, ponte, prezzo)
        self.stile=stile


class CabinaAnimali(CabineStandard):
    def __init__(self, codice, letti, ponte, prezzo, numeroAnimali):
        super().__init__(codice, letti, ponte, prezzo)
        self.numeroAnimali=numeroAnimali
