i=1
j=1
while i<11:
    j=1
    while j<11:
        print("{} x {} = ".format(i,j),i*j)
        j+=1
    print("\n")
    i+=1 

control=False
total=0
print("Girilen sayilari toplama programine hos geldiniz! (Cikis icin C)")
while control==True:
    answer = input("Sayiniz: ")
    if answer.isdigit():
        total += int(answer)
    else:
        if answer == "C" or answer == "c":
            control = False
        else: 
            print("Lütfen sayi giriniz! ya da cikis icin C")

print("Girilen sayilari toplami: ",total)

print("1 - 50 arasindaki cift sayilar(1 ve 50 dahil): \n")
i=0
while i<51:
    i+=1
    if i%2==0:
        print(i)
    else:
        continue
    
