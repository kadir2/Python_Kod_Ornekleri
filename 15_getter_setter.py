import numbers

class products:
    
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.__price = price


    @property
    def al(self):
        return "abcdefg"


    @property       # Read-Only 
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, x):
        if isinstance(x,numbers.Number): #bir sayı olup olmadığını anlamak için
            self.__price = x
        else:
            print(f"{x} bir sayı değil, string")


        


urun1 = products(10, 100)
urun2 = products(20, 200)


print(urun1.al)

urun1.price = 90

print(urun1.price)
