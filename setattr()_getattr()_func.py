class öğrenciler:
    def __init__(self,isim, numara):
        self.isim = isim
        self.numara = numara

öğrenci1 = öğrenciler("Ali", 123)

isim = getattr(öğrenci1, "isim")
print(isim)  # Çıktı: Ali

# getattr ile var olmayan bir özellik çağırma
soyad = getattr(öğrenci1, "soyad", "Soyad bulunamadı")
print(soyad)  # Çıktı: Soyad bulunamadı


# özellik güncelleme
setattr(öğrenci1, "numara", 456)
print(öğrenci1.numara)  # Çıktı: 456

# yeni bir özellik ekleme
setattr(öğrenci1, "soyad", "Yılmaz")
print(öğrenci1.soyad)  # Çıktı: Yılmaz
