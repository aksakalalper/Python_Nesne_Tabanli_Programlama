class Kedi():
    def ses(self):
        print('miyav')
    

class Kopek():
    def ses(self):
        print('hav hav')

class Kus():
    def ses(self):
        print('cik cik')

def HayvanSesi(hayvan):
    hayvan.ses()

ke=Kedi()
ko=Kopek()
ku=Kus()

HayvanSesi(ke)
HayvanSesi(ko)
HayvanSesi(ku)

##sinif icindeki ortak fonksiyonlara ayri ayri gonderilen objeleri kullanmayi saglar.