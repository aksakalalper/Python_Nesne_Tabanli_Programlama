class Araba():
     ## __init__ fonksiyonu ile referans atamalari yapildi.
     # attributeslar verildi.
     def __init__(self,kapiSayisi,renk,marka,model,motorHacmi,arabaFiyati):
        self.kapiSayisi=kapiSayisi
        self.renk=renk
        self.marka=marka
        self.model=model
        self.motorHacmi=motorHacmi
        self.__arabaFiyati=arabaFiyati 
     # metod tanimlandi.
     def MotorHacmiGoster (self):
          print(f'motor hacmi {self.motorHacmi}')
     # metod tanimlandi.
     def KapiSayisiGoster(self):
         print(f'araba kapi sayisi: {self.kapiSayisi}\n')
     # metod tanimlandi.
     def MarkaModelBilgisiGetir(self):
         print(f'araba markasi {self.marka} ve modeli {self.model}')
     # encapsulation ypailarak bilgi okundu.
     def GetArabaFiyati(self):
          return self.__arabaFiyati
     
# inheritance yapildi ve ilave bir attributes eklendi.
class AgirVasita(Araba):
     def __init__(self, kapiSayisi, renk, marka, model, motorHacmi,arabaFiyati,tekerSayisi):
        super().__init__(kapiSayisi, renk, marka, model, motorHacmi,arabaFiyati)
        self.tekerSayisi=tekerSayisi #ilave attributes tanimlandi.
          
     def TekerSayisiGetir(self):
         print(f'agir vasita teker sayisi: {self.tekerSayisi}')

class ArabaSesi():
    def sesCikar(self):
        print('dat dat dat!')

class AgirVasitaSesi():
    def sesCikar(self):
        print('daaaaaat!')

#polymorphism yapilarak her araca ozel korna sesi cikarildi
def KornaSesi(korna):
    korna.sesCikar()   

araba1=Araba(5,'mavi','honda','civic',1600,1600000)
araba2=Araba(3,'kirmizi','audi','a3',2000,3500000)
kamyon1=AgirVasita(2,'beyaz','man','tf300',3500,5000000,18)

araba1KornaSesi=ArabaSesi()
araba2KornaSesi=ArabaSesi()
kamyon1KornaSesi=AgirVasitaSesi()
KornaSesi(kamyon1KornaSesi)
KornaSesi(araba1KornaSesi)
KornaSesi(araba2KornaSesi)





