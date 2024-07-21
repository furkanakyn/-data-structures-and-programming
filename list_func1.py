liste = [10,20,30,40,50]
toplam=sum(liste) #sum listedeki sayıları toplar 
print(toplam,"\n")

liste2 = [1,2,3,4,5]
print(liste2)

del liste2[0:2] #del listede silme işlemi yapar
print(liste2)
del liste2[2]
print(liste2,"\n")

liste3 = [12,10,31,3,0,9,7,18,54,89,62]
print(liste3)
print(sorted(liste3)) #sorted listeyi sıralar (yeni liste oluşmaz)
print(sorted(liste3, reverse=True)) #reverse tersine çevirir

isimler=["Furkan","Yavuz","Muhammmet","Osman","Emir","Abdurrahman"]
print(sorted(isimler, key=len, reverse=True),"\n") 

liste4 = [1,2,3,4,5]
print(liste4)
liste4.append(6)  #append listeye sondan ekleme yapar
list.append(liste4,7)
print(liste4,"\n")

liste5 = [10,20,30]
print(liste5)
liste5.insert(1,15)  #insert liste aralarına ekleme yapar
list.insert(liste5,3,25)
print(liste5,"\n")

liste6 = [1,2,3,4,5]
print(liste6)
eklenecek = [6,7,8,9]
eklenecek2 = [10]
print(eklenecek,"\n")
liste6.extend(eklenecek) #extend listeleri birbirine ekler
list.extend(liste6,eklenecek2)
print(liste6,"\n")

