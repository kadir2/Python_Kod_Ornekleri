sozluk = {"bir":1, "iki":2, "uc":3}


print(sozluk["bir"]) # 1

print(sozluk) # {'bir': 1, 'iki': 2, 'uc': 3}


for i in sozluk:  # sadece keyleri alır
   print(i)


for i in sozluk.items(): # key ve value alır
   print(i) 


for i,j in sozluk.items():
   print(i,j) # key ve value alır   

