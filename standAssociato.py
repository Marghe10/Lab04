class StandAssociato:
    def __init__(self, codice_stand, codice_espositore):
        self.codice_stand = codice_stand
        self.codice_espositore = codice_espositore

    def __str__(self):
        return str(self.codice_stand) + str(self.codice_espositore)