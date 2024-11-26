with open("text.txt", "r") as dosya:
    dosya.seek(6)
    print(dosya.read())


    dosya.seek(0)
    str = dosya.read(5) # 5 karakter oku
    print(str)
