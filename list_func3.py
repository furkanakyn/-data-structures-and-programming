sehirler = ["İstanbul","Ankara","Trabzon","Tekirdag","Konya"]
print("Orijinal hali: ",sehirler)
sehirler.sort() #sort listeyi sıralar !!! sorted'dan farkı listenin kendisi değişir
print("Sort edilmiş hali: ", sehirler)

sehirler.reverse() #reverse listeyi tersine çevirir
print("Reverse edilmiş hali: ",sehirler)
list.reverse(sehirler)
print("2. Reverse edilmiş hali: ",sehirler,"\n")



sehirler2 = ["Hakkari","Artvin","Van","Balikesir","Canakkale",7,11,4]
print("Orijinal hali: ",sehirler)
list.sort(sehirler2, key=str)
print("Sort edilmiş hali: ",sehirler2)

