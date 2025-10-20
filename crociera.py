import csv
from passeggeri import Passeggeri
from cabine import CabineStandard,CabinaAnimali,CabinaDeluxe
import operator

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome=nome
        self.cabine=[]
        self.passeggeri=[]

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            file=open(file_path,"r")
            reader = csv.reader(file)
            for riga in reader:
                if len(riga)==3:
                    codicePasseggeri,nome,cognome=riga
                    passeggero=Passeggeri(codicePasseggeri,nome,cognome)
                    self.passeggeri.append(passeggero)
                elif len(riga)==4:
                    codice,letti,ponte,prezzo=riga
                    cabinaS=CabineStandard(codice,letti,ponte,int(prezzo))
                    self.cabine.append(cabinaS)
                elif len(riga)==5:
                    if riga[4].isdigit():
                        codice,letti,ponte,prezzoBase,numeroAnimali=riga
                        # numeroAnimali = int(riga[4])
                        # prezzoBase = int(riga[3])
                        prezzoFinale = int(prezzoBase) * (1 + 0.10 * int(numeroAnimali))
                        CabinaA=CabinaAnimali(codice,letti,ponte,prezzoFinale,numeroAnimali)
                        self.cabine.append(CabinaA)
                    else:
                        codice,letti,ponte,prezzoBase,stile=riga
                        prezzoFinale = int(prezzoBase)*1.20
                        CabinaD = CabinaDeluxe(codice, letti, ponte, prezzoFinale, stile)
                        self.cabine.append(CabinaD)

        except FileNotFoundError:
            print("il file da te inserito non è stato trovato")

        print("Stampo le cabine per verifica")
        for c in self.cabine:
            print(f"{c.codice}")

        print("Stampo i passeggeri per verifica")
        for p in self.passeggeri:
            print(f"{p.codice} {p.nome} {p.cognome}")

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""

        cabina_da_prenotare = None
        for x in self.cabine:
            if x.codice == codice_cabina:
                if x.disponibile == False:
                    raise Exception(f"Cabina già prenotata: {codice_cabina}")
                else:
                    cabina_da_prenotare = x

        if cabina_da_prenotare is None:
            raise Exception(f"Codice cabina non trovato: {codice_cabina}")

        passeggero_prenotante = None
        for y in self.passeggeri:
            if codice_passeggero == y.codice:
                if y.assegnato is not None:
                    raise Exception(f"Il passeggero {y.codice} ({y.nome} {y.cognome}) ha già prenotato una cabina!")
                else:
                    passeggero_prenotante = y

        if passeggero_prenotante is None:
            raise Exception(f"Codice passeggereo non trovato: {codice_passeggero}")


        cabina_da_prenotare.disponibile = False
        passeggero_prenotante.assegnato = cabina_da_prenotare.codice

        print(f"Al passeggero {passeggero_prenotante.cognome} {passeggero_prenotante.nome} è stata assegnata la cabina {cabina_da_prenotare.codice}")

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""

        lista_cabine_ordinate = sorted(self.cabine, key=operator.attrgetter('prezzo'))
        return lista_cabine_ordinate
    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        if not self.passeggeri:
            print("Nessun passeggero caricato.")
            return
        for p in self.passeggeri:
            if p.assegnato:
                print(f"{p.codice} - {p.nome} {p.cognome} → Cabina: {p.assegnato}")
            else:
                print(f"{p.codice} - {p.nome} {p.cognome} → Nessuna cabina assegnata")


