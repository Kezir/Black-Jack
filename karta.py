import random
import os,sys
rodzaje = ["trefl", "karo", "kier", "pik"]
nazwy = ["As","2","3","4","5","6","7","8","9","10","Walet","Dama","Krol"]
wartosci = [11,2,3,4,5,6,7,8,9,10,10,10,10]
karty1 = ["AC.png","2C.png","3C.png","4C.png","5C.png","6C.png","7C.png","8C.png","9C.png","10C.png","JC.png","QC.png","KC.png","AD.png","2D.png","3D.png","4D.png","5D.png","6D.png","7D.png","8D.png","9D.png","10D.png","JD.png","QD.png","KD.png","AH.png","2H.png","3H.png","4H.png","5H.png","6H.png","7H.png","8H.png","9H.png","10H.png","JH.png","QH.png","KH.png","AS.png","2S.png","3S.png","4S.png","5S.png","6S.png","7S.png","8S.png","9S.png","10S.png","JS.png","QS.png","KS.png"]
karty = []

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

for i in karty1:
    karty.append(resource_path("Assets/" + i))

empty = [resource_path("Assets/gray_back.png")]

class Karta:
    def __init__(self,rodzaj,nazwa,wartosc,image):
        self.rodzaj = rodzaj
        self.nazwa = nazwa
        self.wartosc = wartosc
        self.image = image

    def __repr__(self):
        return self.rodzaj + " " + self.nazwa + " " + self.wartosc

    def show(self):
        print("{} of {} [points] {} [name] {}".format(self.rodzaj,self.nazwa,self.wartosc,self.image))

class Talia:
    def __init__(self):
        self.talia = []
        self.temp = []
        self.build()
        self.tasowanie()

    def build(self):
        x = 0
        for i in rodzaje:
            for j in range(len(nazwy)):
                self.talia.append(Karta(i,nazwy[j],wartosci[j],karty[x]))
                x = x + 1

    def show(self):
        for i in self.talia:
            i.show()

    def tasowanie(self):
        random.shuffle(self.talia)

class Player:
    def __init__(self,bilans):
        self.reka = []
        self.pozycja = []
        self.bilans = bilans
        self.busted = False
        self.suma = 0
        self.alive = True

    def show(self):
        for i in self.reka:
            i.show()

    def dodaj_karte(self,talia):
        if self.busted == False:
            x = random.sample(talia, 1)[0]
            self.reka.append(x)
            talia.remove(x)
            self.check_sum()

    def check_sum(self):
        self.suma = 0
        for i in self.reka:
            self.suma = self.suma + i.wartosc

        if self.suma > 21:
            for i in self.reka:
                if i.nazwa == "As":
                    self.suma = self.suma - 10
                    if self.suma <= 21:
                        break
            if self.suma > 21:
                self.busted = True


class Krupier:
    def __init__(self):
        self.reka = []
        self.image = empty[0]
        self.suma = 0
        self.tura = 0
        self.busted = False

    def show_first(self):
        self.reka[0].show()

    def show(self):
        for i in self.reka:
            i.show()

    def dodaj_karte(self,talia):
        x = random.sample(talia, 1)[0]
        self.reka.append(x)
        talia.remove(x)
        self.check_sum(talia)

    def check_sum(self,talia):
        self.suma = 0
        for i in self.reka:
            self.suma = self.suma + i.wartosc

        if self.suma > 21:
            for i in self.reka:
                if i.nazwa == "As":
                    self.suma = self.suma - 10
                    if self.suma <= 21:
                        break

        if self.suma <= 16:
            self.dodaj_karte(talia)
            self.check_sum(talia)

class Game:
    def __init__(self,talia,gracze,krupier):
        self.talia = talia
        self.players = gracze
        self.krupier = krupier
        self.start_rozdaj()

    def start_rozdaj(self):
        for every in self.players:
            for i in range(2):
                x = random.sample(self.talia,1)[0]
                every.reka.append(x)
                self.talia.remove(x)
            every.check_sum()
        for i in range(2):
            x = random.sample(self.talia, 1)[0]
            self.krupier.reka.append(x)
            self.talia.remove(x)
        self.krupier.check_sum(self.talia)

# Beniamin Kozyra - rozpoczącie rozgrywki
#def start(ilosc_graczy,bilans):
#    deck = Talia()
#    tablica_graczy = []
#    for i in range(ilosc_graczy):
#        tablica_graczy.append(Player(bilans[i]))

#    krupier = Krupier()
#    return Game(deck.talia, tablica_graczy, krupier)
    #gracz1.dodaj_karte(deck.talia)
    #gracz1.show()
    #print(gracz1.busted)
    #gracz2.show()
    #print(gracz2.busted)
    #krupier.show()
    #print(krupier.busted)
    #print(len(deck.talia))







