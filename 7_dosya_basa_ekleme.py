with open("text.txt", "r+") as dosya:
    data = dosya.read()
    dosya.seek(0)
    data = "ilk cümle\n" + data
    dosya.write(data)
