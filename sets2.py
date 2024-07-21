a ={1,2,3,4,5,6,7}
b={3,5,7}

sonuc = a.isdisjoint(b) #ayrık küme durumunu inceler
# sonuc = set.isdisjoint(a,b)
print(sonuc)

kume1={"a","d","e"}
kume2={"a","b","c","d","e","f"}

aksonuc= kume1.issubset(kume2) #alt küme olma durumunu inceler
# ksonuc= set.issubset(kume1,kume2)
print(aksonuc)

uksonuc= kume2.issuperset(kume1) #üst küme olma durumunu inceler
print(uksonuc)

birlesim= set.union(a,b) #küme birlesimi yapar
print(birlesim,"\n")

fark = a.difference(b) #küme farkı alır
print(a,"-",b, "=", fark) 