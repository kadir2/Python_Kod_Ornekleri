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


deger_al()


con.close()


