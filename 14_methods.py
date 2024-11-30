import csv


class products:
    
    all = []

    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

    def __repr__(self):  #bu methodu tanımlamazsak print(urun1) dediğimizde <__main__.products object at 0x0000022D0B6F5B20> şeklinde bir çıktı alırız.
        return f'products({self.quantity}, {self.price})' # __str__ yerine __repr__ kullanırsak daha detaylı bilgi verir. 

    @classmethod       # classdan bağımsız çalışır
    def csv_file(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for itemm in items:
            print(itemm)


    @staticmethod
    def suphelen(num):
        if isinstance(num, float): 
            return num.is_integer() #float bir sayının tam sayı olup olmadığını kontrol eder. Eğer tam sayı ise True döner.

        elif isinstance(num,int): #int bir sayının tam sayı olup olmadığını kontrol eder. Eğer tam sayı ise True döner.
            return True

        else:
            return False

       

urun1 = products(10, 100)
urun2 = products(20, 200)

#print(urun1)    #products(10, 100)

products.csv_file()


print(products.suphelen(7.34))
