sayi1= input("Birinci sayiyi giriniz: ")
sayi2= input("İkinci sayiyi giriniz: ")


try:
      sayi1= int(sayi1)
      sayi2= int(sayi2)
      print(sayi1/sayi2)

except ValueError:
   print("Lütfen sadece sayi giriniz!")

except ZeroDivisionError:
   print("Bir sayi sifira bolunemez!")

  

