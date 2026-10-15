import csv
from standStandard import StandStandard
from standPremium import StandPremium
from standPrese import StandPrese
from espositori import Espositori

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.standard=[]
        self.prese=[]
        self.premium=[]
        self.espositori=[]

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        with open(file_path, "r") as file:
            lettore=csv.reader(file)
            for riga in lettore:
                codice=riga[0]
                prima_lettere_codice=codice[0]
                if prima_lettere_codice == "S":
                    codice=riga[0].strip()
                    superficie=riga[1].strip()
                    padiglione=riga[2].strip()
                    prezzo=riga[3].strip()
                    if len(riga) == 4:
                        stand_standard=StandStandard(codice,superficie,padiglione,prezzo)
                        self.standard.append(stand_standard)
                    elif len(riga) == 5:
                        ultima=riga[-1].strip()
                        if ultima.isdigit():
                            numero_prese=ultima
                            stand_prese=StandPrese(codice,superficie,padiglione,prezzo,numero_prese)
                            self.prese.append(stand_prese)
                        else:
                            posizione=ultima
                            stand_premium=StandPremium(codice,superficie,padiglione,prezzo,posizione)
                            self.premium.append(stand_premium)
                else:
                    codice_e=riga[0].strip()
                    nome=riga[1].strip()
                    cognome=riga[2].strip()
                    espositore=Espositori(codice_e,nome,cognome)
                    self.espositori.append(espositore)

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        tutti_gli_stand=self.standard + self.prese + self.premium
        stand_ordinati_per_prezzo=sorted(tutti_gli_stand, key=lambda s:float(s.prezzo))
        return stand_ordinati_per_prezzo
                    # lo posso fare perchè tutte e tre le liste che ho unito insieme hanno il parametro
                    # prezzo, quindi la lista che ho creato con tutti gli stand al suo interno avrà un
                    # parametro prezzi con i pressi di tutti gli stand
