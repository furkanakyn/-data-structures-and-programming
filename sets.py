degerler = {1,3,5,"a","c",34+2j,(100,200,300),2,3,4,5}
print(degerler,"\n")

a = {1,3,5,7}
b = {1,2,3,4,5}
c = {4,5,6,7,8,9,10}
d = {12,13}
toplam = a | b | c  # | ile  kümelerde toplama yapılır aynı degerler tekrarlanmaz
print(toplam,"\n")

kesisim = a & b & c # & kesisim(ortak) elemanlar alınır
print(kesisim,"\n")

fark = a - b # a ' dan b'de olan elemanları cıkarır
print(fark,"\n")

simetrik_fark = a ^ b  #farklı olan elemanları alır
print(simetrik_fark,"\n")

set.add(a,8)  #add deger ekler
c.add(11)
print(a,"\n")

c.update(d) #update ekleme yapar
print(c,"\n")

d.clear() #clear kümeyi temizler
print(d,"\n")


c.remove(10)
c.discard(10)  #discard ve remove deger siler ama remove olmayan degerler icin hata mesajı verir
print(c,"\n")

print("Orijinal a: ",a)
deger= a.pop() #rastgele bir degeri siler
print("Cikarilan değer: ",deger)
print("Son hali:",a)