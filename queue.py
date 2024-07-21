class Queue:
    def __init__(self):
        self.items =[]
        print("Kuyruk Olusturuldu.")
        
    def __str__(self):
        elemanlar = [str(x) for x in self.items]
        return '\n'.join(elemanlar)
    
    def enqueue(self,deger):
        self.items.append(deger)
        return print("Eleman kuyruğa eklendi")

kuyruk =  Queue()
kuyruk.enqueue(5)
kuyruk.enqueue(10)
print(kuyruk)