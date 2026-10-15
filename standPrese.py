class StandPrese(object):
    def __init__(self,codice,superficie,padiglione,prezzo,numero_prese):
        self.codice = codice
        self.superficie = superficie
        self.padiglione = padiglione
        self.prezzo = prezzo
        self.numero_prese = numero_prese

    def __str__(self):
        return str(self.codice) + str(self.superficie) + str(self.padiglione) + str(self.prezzo)