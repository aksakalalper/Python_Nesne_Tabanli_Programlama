#class 
class Kisi:
    pass
    #class attributes (her zaman kullanılmayacak ozellikler burda olur)
    adres='bilgi yok'
    #object attributes (devamli kullanilacak seyler burda olur)
        #constructor (yapici metod)
    def __init__(this,isim,yas): #object uzerine eklenecek bilgileri aktarır
            this.isim=isim
            this.yas=yas
            print('init metodu calisti')

    #methods


#object/instance
k1=Kisi('ahmet',29)
k2=Kisi('ayse',25)
print(k1) #iki ayri kisinin de adresleri ayri ayri oluyor.
print(type(k1)) 
print(k2) #iki ayri kisinin de adresleri ayri ayri oluyor.
print(type(k2))
#updating
k1.isim='mehmet'
k2.adres='izmir'
#accessing object attriutes
print(f'isim: {k1.isim}, yas: {k1.yas}')
print(f'isim: {k2.isim}, yas: {k2.yas} adres: {k2.adres}')

class aileUyeleri:
      pass
      adres='cigli/evka5'

      def __init__(this,ad,soyad,yas,meslek):
            this.ad=ad
            this.soyad=soyad
            this.yas=yas
            this.mesles=meslek
            print('bilgiler okundu.')

kisi1=aileUyeleri(ad='alper',soyad='aksakal',yas=29,meslek='muhendis')
kisi2=aileUyeleri(ad='alptekin',soyad='aksakal',yas=14,meslek='ogenci')
kisi3=aileUyeleri(ad='murat',soyad='aksakal',yas=55,meslek='polis')
kisi4=aileUyeleri(ad='isminur',soyad='aksakal',yas=52,meslek='hemsire')



print(f'aile uyeleri sirasiyla:{kisi1.ad}, {kisi2.ad}, {kisi3.ad}, {kisi4.ad}')

