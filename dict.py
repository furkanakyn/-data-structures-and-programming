kisi= {
    "Ad" : "Osman",
    "Soyad" : "Akyün",
    "Yas" : 21,
    "Cinsiyet" : "Erkek",
    "Telefon" : "0505 505 5505",
    "Gereksizb" : "Abubugu"
}

print(kisi,"\n")
kisi["Ad"]="Furkan"
del kisi["Gereksizb"]
print(min(kisi),"\n")

iletisim = {
    "Adres" : ["İstanbul","Tokat"],
    "Telefon" : "0539 123 4567",
}

kisi.update(iletisim)
print(kisi,"\n")

print(kisi.get("Adres")) #get islemi cagırma yapar
print(kisi.get("adres")) #cagıracak degisken yoksa None doner
print(kisi.get("adres","Boyle bir degisken yok"), "\n") # None yerine verilecek uyarıyı degistirebiliriz

tcnum = kisi.setdefault("TC", 12345678910) #set default ile degisken ekleyebiliriz, deger vermezsek none olarak eklenir
print(kisi["TC"],"\n")


kisi.pop("TC") #pop ile del gibi silme işlemi yaparız

ogrenci = {"İsim":"Furkan","Not":2.9,"Donem":2024}
print(ogrenci.keys()) #anahtar kelimelerini söyler
print(ogrenci.values()) #degerleri söyler
print(ogrenci.items()) #anahtar kelimelerini değerleri ile söyler

aylar = {"Ocak","Subat","Mart","Nisan"}
maas= dict.fromkeys(aylar,0) #fromkeys hepsinin degerini atar
print(maas)


renkler ={"Beyaz":"White","Mavi":"Blue","Siyah":"Black","Yeşil":"Green","Sari":"Yellow"}

for anahtar in renkler:
    print(renkler[anahtar])
