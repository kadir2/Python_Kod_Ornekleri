import sqlite3
import random
import time
import datetime


con = sqlite3.connect("ders.db")
cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS tablo1 (zaman REAL, tarih TEXT, anahtarkelime TEXT, deger REAL)")

def ekle():
   zaman = time.time()
   tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
   anahtarkelime = "python sqlite"
   deger = random.randrange(0,10)
   cursor.execute("INSERT INTO tablo1(zaman,tarih,anahtarkelime,deger) VALUES(?,?,?,?)",(zaman,tarih,anahtarkelime,deger))
   con.commit()


def deger_al():
    cursor.execute("SELECT * FROM tablo1 ")     

    # ("SELECT zaman,tarih From tablo1") sadece taman ve tarihi al
    # ("SELECT * From tablo1 WHERE deger = 2") değerleri 2 olan satırları al

    data = cursor.fetchall() #gelen değerleri değişkene ata
    for i in data:
        print(i)


def sil_guncelle():
    cursor.execute("SELECT * FROM tablo1 ")     

    # ("SELECT zaman,tarih From tablo1") sadece taman ve tarihi al
    # ("SELECT * From tablo1 WHERE deger = 2") değerleri 2 olan satırları al

    data = cursor.fetchall() #gelen değerleri değişkene ata
    print("İlk değerler:")
    for i in data:
        print(i)




    cursor.execute("UPDATE tablo1 SET deger = 99 WHERE deger = 5")
    cursor.execute("SELECT * FROM tablo1 ")     

    data = cursor.fetchall() #gelen değerleri değişkene ata
    print("Güncellendikten sonra değerler:")
    for i in data:
        print(i)


    cursor.execute("DELETE FROM tablo1 WHERE deger=7")
    cursor.execute("SELECT * FROM tablo1 ")     

    # ("SELECT zaman,tarih From tablo1") sadece taman ve tarihi al
    # ("SELECT * From tablo1 WHERE deger = 2") değerleri 2 olan satırları al

    data = cursor.fetchall() #gelen değerleri değişkene ata
    print("Sildikten sonraki değerler:")
    for i in data:
        print(i)

    con.commit()





sil_guncelle()

con.close()
