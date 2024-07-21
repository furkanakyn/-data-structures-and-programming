sayilar = [1,4,3,1,1,2,4,5,6,7,2,1,5,6,3,7,8,0,6,4,2,4,3,8,7,4,3,1,2,4,0]
print(sayilar)
adet = sayilar.count(4) #count ifadesi değerin listede kaç adet olduğu bilgisini verir
adet2 = list.count(sayilar,3)
print("4 sayisi listede {} adettir".format(adet))
print("%d sayisi listede %d adettir."%(3,adet2),"\n")

sayilar2 = [1,2,6,7,22,9,0,5,3,4]
print(sayilar2)
sira= sayilar2.index(4) #index aranan değerin kaçıncı indeks de olduğu bilgisini verir
sira2=list.index(sayilar2,5,7,11)    #(aranan deger , baslangic , bitis ) seklinde de olabilir
print("4 sayisi listenin %d sirasindadir"%sira)
print("5 sayisi listenin %d sirasindadir"%sira2,"\n")

a = [10,20,30,40,50]
b = list.copy(a) # a.copy() # a[:] seklinde de olabilir

print("a listesi",a,id(a))
print("b listesi",b,id(b),"\n")

a[0]=89
b[1]=53

print("a listesi",a,id(a))
print("b listesi",b,id(b))