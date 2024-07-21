liste=[23,1235,22,1,4,7,4,300,500]
for i in range(1,11):
        for j in range(1,11):
                print("{} x {} = ".format(i,j),i*j)
        print("\n") 



baslangic=int(input("Baslangic sayisini giriniz: "))
bitis=int(input("Bitis sayisini giriniz: "))

for i in range(baslangic,bitis+1):
    print(i)


baslangic=int(input("Baslangic sayisini giriniz: "))
bitis=int(input("Bitis sayisini giriniz: "))
sayi=0
for i in range(baslangic,bitis+1):
    sayi+=i

print(baslangic, "ile" , bitis, "arasindaki sayilarin toplami: ",sayi)


baslangic=int(input("Baslangic sayisini giriniz: "))
bitis=int(input("Bitis sayisini giriniz: "))
sayi=0
for i in range(baslangic,bitis+1):
    if i%2==0:
        sayi+=i

print(baslangic, "ile" , bitis, "arasindaki cift sayilarin toplami: ",sayi)

total=int(input("Kac satir olsun: "))
for i in range(total):
    print("*"*(i+1)) 

total=int(input("Kac satir olsun: "))
if total>0:
    for i in range(total):
        star = "*" * (((i+1)*2)-1)
        print(star.center(total*2))   
else:
    print("Gecerli bi sayi adeti giriniz!")

