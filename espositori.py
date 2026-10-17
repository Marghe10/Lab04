class Espositori(object):
    def __init__(self,codice,cognome,nome):
        self.codice = codice
        self.cognome = cognome
        self.nome = nome

    def __str__(self):
        return f"codice: {str(self.codice)}, cognome: {str(self.cognome)}, nome: {str(self.nome)}"
