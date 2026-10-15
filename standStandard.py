class StandStandard(object):
    def __init__(self,codice,superficie,padiglione,prezzo):
        self.codice = codice
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo = prezzo

    def __str__(self):
        return str(self.codice) + str(self.superficie) + str(self.padiglione) + str(self.prezzo)