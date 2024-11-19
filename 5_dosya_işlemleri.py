f =open("text.txt", "w+")



for i in range(1,11):
   f.write("Hello World"+str(i)+"\n")



f.seek(0) # dosya başına git
print(f.read())

f.close()

