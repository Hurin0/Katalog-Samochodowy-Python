from samochod import Samochod
import os

class Katalog:

    def __init__(self, file_path):

        self.file_path = file_path


    def wczytajListe(self):

        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                lines = f.readlines()
            n=7
            samochody = [lines[i:i + n] for i in range(0, len(lines), n)]
        else:
            input('plik nie istnieje')
    
        
        self.obj_sam = []
        for sam in samochody:
            sam.pop()
            self.obj_sam.append(Samochod(*sam))


    def wypiszListe(self):
        for c, i in enumerate(self.obj_sam):
            print(c+1)
            print(i.getMarka())
            print(i.getModel())
            print(i.getPojemnosc())
            print(i.getPrzebieg())
            print(i.getRocznik())
            print(i.getTypSkrzyni())
        input('nacisnij aby kontynuowac')


    def dodajSamochod(self):
        
        sam = []
        sam.append(input('podaj marke: '))
        sam.append(input('podaj model: '))
        sam.append(input('podaj rocznik: '))
        sam.append(input('podaj pojemnosc: '))
        sam.append(input('podaj przebieg: '))
        sam.append(input('podaj typ skrzyni: '))
        sam.append('--------------')

        if os.path.exists(self.file_path):
            with open(self.file_path, 'a') as f:
                for l in sam:
                    f.write(f'\n{l}')
        else:
            input('plik nie istnieje')

        sam.pop()
        self.obj_sam.append(Samochod(*sam))

    
    def usunSamochod(self):
        
        ktory = input('ktory usunac: ')
        self.obj_sam.pop(int(ktory))

        # if os.path.exists(self.file_path):
        #     open(self.file_path, 'w').close()
        #     with open(self.file_path, 'w') as f:
        #         lines = f.readlines()
        #     n=7
        #     samochody = [lines[i:i + n] for i in range(0, len(lines), n)]
        # else:
        #     input('plik nie istnieje')



    def wyswietlenieWarunkowe(self):
        warunek = input('rocznik warunkowy: ')

        samPoWar = [obj for obj in self.obj_sam if obj.getRocznik() < warunek]
        for sam in samPoWar:
            print(sam.getModel())
            print(sam.getModel())
            print(sam.getPojemnosc())
            print(sam.getPrzebieg())
            print(sam.getRocznik())
            print(sam.getTypSkrzyni())
        input('nacisnij aby kontynuowac')


    def wyswietlJeden(self):

        ktory = input('ktory wyswietlic: ')
        print(self.obj_sam[int(ktory)-1].getMarka())
        print(self.obj_sam[int(ktory)-1].getModel())
        print(self.obj_sam[int(ktory)-1].getPojemnosc())
        print(self.obj_sam[int(ktory)-1].getPrzebieg())
        print(self.obj_sam[int(ktory)-1].getRocznik())
        print(self.obj_sam[int(ktory)-1].getTypSkrzyni())
        
        input('nacisnij aby kontynuowac')


    def posortujPrzebiegiem(self):
        
        import operator
        sorted_x = sorted(self.obj_sam, key=operator.attrgetter('przebieg'))

        for c, i in enumerate(sorted_x):
            print(c)
            print(i.getMarka())
            print(i.getModel())
            print(i.getPojemnosc())
            print(i.getPrzebieg())
            print(i.getRocznik())
            print(i.getTypSkrzyni())

        input('nacisnij aby kontynuowac')