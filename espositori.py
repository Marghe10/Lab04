class Espositori(object):
    def __init__(self,codice,cognome,nome):
        self.codice = codice
        self.cognome = cognome
        self.nome = nome

    def __str__(self):
        return str(self.codice) + str(self.cognome) + str(self.nome)