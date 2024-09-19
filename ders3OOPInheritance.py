#inheritance(kalitim): miras alma

#kisi->isim,soyisim,yas,yemekye(),uyu() 
#ogrenci(kisi),ogretmen(kisi) ogrenci ve ogretmen de isim soyisim yas  ve yemek yeme fonksiyonlarina sahip olur.

#haycan-> kopek(hayvan),kedi(hayvan)

class kisi():
    def __init__(self,isim,soyisim,yas):
        self.isim=isim
        self.soyisim=soyisim
        self.yas=yas
        print('kisi yaratildi.')

    def ben_kimim(self):
        print('ben bir kisiyim.')
    
    def yemek_ye(self):
        print('yemek yiyorum.')

class ogrenci(kisi):
    def __init__(self,isim,soyisim,yas,numara):
        kisi.__init__(self,isim,soyisim,yas)
        self.numara=numara
        print('ogrenci yaratildi')
    
    #overwrite
    def ben_kimim(self):
        print('ben ogrenciyim.')

class ogretmen(kisi):
    def __init__(self, isim, soyisim, yas,brans):
        super().__init__(isim, soyisim, yas)
        self.brans=brans
    def benKimim(self):
            print('ben ogretmenim.')

        
        
kisi1=kisi(
    isim='mehmet',
    soyisim='yilmaz',
    yas=22
)     

ogrenci1=ogrenci(
    isim='ahmet',
    soyisim='yilmaz',
    yas=29,
    numara='112233'
)

ogretmen1=ogretmen(
    isim='ayse',
    soyisim='yilmaz',
    yas=39,
    brans='matematik'
)

print(f'yaratilan ogrenci {ogrenci1.isim} {ogrenci1.soyisim} ve yas {ogrenci1.yas} ve numarasi {ogrenci1.numara}')
print(f'yaratilan kisi {kisi1.isim} {kisi1.soyisim} ve yas {kisi1.yas}')

ogrenci1.ben_kimim()
kisi1.yemek_ye()
ogretmen1.benKimim()
