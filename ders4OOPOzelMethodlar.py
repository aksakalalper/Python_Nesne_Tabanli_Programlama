class film():
    def __init__(self,adi,direktor,sure):
        self.adi=adi
        self.direktor=direktor
        self.sure=sure
        print('film olusturuldu.')
    def __str__(self):
        return self.direktor

film1=film('logan','stan lee',1.30)
print(f'film adi {film1.adi} film direktoru {film1.__str__()}')


