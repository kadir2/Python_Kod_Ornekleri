class products:
    
    oran = 10
    all = []

    def __init__(self,name, quantity, price):

        assert quantity > 0, f"miktar {quantity} 0 dan büyük olmalı"
        assert price > 0, f"fiyat {quantity} 0 dan büyük olmalı"

        self.name = name
        self.quantity = quantity
        self.price = price

        products.all.append(self)  # her oluşturulan ürünü all listesine ekler 


    def calculate(self):
        self.price = self.price * products.oran     # oranı sınıf değişkeni olarak tanımladığımız için sınıf üzerinden değişebilir





urun1 = products("elma", 10, 5)
urun2 = products("armut", 20, 10)




print(products.__dict__) # {'__module__': '__main__', 'oran': 1.5, '__init__': <function products.__init__ at 0x7f8b1c1b7d30>, '__dict__': <attribute '__dict__' of 'products' objects>, '__weakref__': <attribute '__weakref__' of 'products' objects>, '__doc__': None}
print(urun1.__dict__) # {'name': 'elma', 'quantity': 10, 'price': 5}

#print(urun1.oran)      # 1.5
#print(products.oran)       # 1.5

urun1.calculate()
print(urun1.price)      # 50



urun2.oran = 20
urun2.calculate()
print(urun2.price)      # 100, 200 değil. Değişmedi çünkü oran sınıf değişkeni olarak tanımlandı ve sınıf üzerinden değiştirilebilir



# print(products.all)     # [<__main__.products object at 0x7f8b1c1b7d60>, <__main__.products object at 0x7f8b1c1b7d90>]


for instance in products.all:
    print(instance.name)     # elma, armut
