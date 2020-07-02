

class Samochod:

    def __init__(self, marka, model, rocznik, pojemnosc, przebieg, typ_skrzyni):
        
        self.marka = marka
        self.model = model
        self.rocznik = rocznik
        self.pojemnosc = pojemnosc
        self.przebieg = int(przebieg)
        self.typ_skrzyni = typ_skrzyni


    def setMarka(self, marka):
        self.marka = marka

    def setModel(self, model):
        self.model = model
    
    def setPojemnosc(self, pojemnosc):
        self.pojemnosc = pojemnosc

    def setPrzebieg(self, przebieg):
        self.przebieg = int(przebieg)

    def setRocznik(self, rocznik):
        self.rocznik = rocznik

    def setTyp_skrzyni(self, typ_skrzyni):
        self.typ_skrzyni = typ_skrzyni
  
    def getMarka(self):
        return self.marka

    def getModel(self):
        return self.model

    def getPojemnosc(self):
        return self.pojemnosc

    def getPrzebieg(self):
        return self.przebieg

    def getRocznik(self):
        return self.rocznik

    def getTypSkrzyni(self):
        return self.typ_skrzyni


