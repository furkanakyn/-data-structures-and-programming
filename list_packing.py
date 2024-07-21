liste = [10,20,30]
a,b,c= liste
print(a,b,c,"\n")

liste = [10,20,30,40,50]
a,*b ,c = liste
print(a),print(b),print(c,"\n")

liste = [10,20,30]
a,_,_= liste
print(a,"\n")

a=[10,20,30]
b=[40,50,60]
c=[*a,*b]
print(c,"\n")

b=[11,22,33]
[*a]=b
print(a,"\n")

word = "Python"
l1,l2,l3,*l4 =word
print(l1,l2,l3,l4,"\n")