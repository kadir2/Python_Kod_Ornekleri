import sqlite3

con = sqlite3.connect("ders.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT , soyad TEXT , numara INT)") # Tablo oluşturuyoruz.


def ekle():
    cursor.execute("INSERT INTO ogrenciler VALUES('MUSTAFA', 'MAYA', '8346')") # Veritabanına veri ekliyoruz.
    con.commit() # İşlemi bitiriyoruz.
    con.close() # Bağlantıyı koparıyoruz.



tablo_olustur() # Fonksiyonu çağırıyoruz.    
ekle() # Fonksiyonu çağırıyoruz.
