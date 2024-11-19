try:
   dosya = open("dosya.txt")

except IOError:
   print("Dosya bulunamadi")

finally:      #daha guvenli bir hale getirmek icin finally kullanilir
   dosya.close()  #hata versin veya vermesin dosyayi kapat
