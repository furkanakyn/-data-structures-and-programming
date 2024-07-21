liste = [1,2,3,4,5,6,7,8,9,10]
yeni = []
for i in liste:
    yeni.append(i)
print(yeni)

yeni = [i for i in liste]
print(yeni,"\n")

list = []
elemanlar = []
for x in list:
    elemanlar.append(str(x))

elemanlar = [str(x) for x in list]