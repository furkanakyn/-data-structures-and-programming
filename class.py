class Animal():
    name = "Hayvan"
    print("Sinifin icindeki print")
print("Sinifin disindaki print")

class Hayvan():
    def __init__(self, name):
        print("Hayvan sinifi olusturuldu")
        print(f"{name} degeri geldi")

    
nesne = Hayvan("Papagan")
