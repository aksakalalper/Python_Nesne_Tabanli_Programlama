class BankAccount():
    def __init__(self,name,money,adress):
        self.name=name #public degisken oldu
        self.__money=money #private degisken oldu
        self.adress=adress

    #get ve set ile alinir
    def GetMoney(self): 
        return self.__money  #ancak bu sekilde private degisken alinir.
     
    def SetMoney(self,amount):
        self.__money=amount


p1=BankAccount('ahmet',16000,'istanbul')
print(p1.adress)
print(p1.GetMoney()) 
p1.SetMoney(2000)
print(p1.GetMoney()) 