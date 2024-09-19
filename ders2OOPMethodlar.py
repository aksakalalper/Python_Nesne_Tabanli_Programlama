class xxx():
    def __init__(self) -> None:
        pass

    #instance methods
    def intro(self):
        print('giris yapildi')

    def yasHesapla(self,dogumYili):
        self.dogumYili=dogumYili
        return 2024-dogumYili

#object instance
k1=xxx()

k1.intro()
print(k1.yasHesapla(1995))

class daire:
    pi=3.14

    def __init__(self,yaricap):
        self.yaricap=yaricap

    #methodlar
    def cevreHesaplama(self):
        return 2*self.pi*self.yaricap
    
    def alanHesaplama(self):
        return self.pi*(self.yaricap**2)
    

d1=daire(5)

print(f'dairenin yaricapi {d1.yaricap} dairenin cevresi {d1.cevreHesaplama()} dairenin alani {d1.alanHesaplama()}')
        
        
