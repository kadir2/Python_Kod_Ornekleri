with open("text.txt", "r+") as dosya:
    data = dosya.readlines()
    data.insert(2, "Bu satir dosyaya eklendi.\n") # Ucuncu satira ekleme yapılır.
    dosya.seek(0)
    dosya.writelines(data) # Dosyaya yazma işlemi yapılır.
