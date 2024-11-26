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


tablo_olustur()

i=0
while(i<10):
    ekle()
    i+=1
    time.sleep(0.5)

con.close()
