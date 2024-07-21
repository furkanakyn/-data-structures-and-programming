class TreeNode:
    def __init__(self,veri, cocuklar=[]):
        self.veri = veri
        self.cocuklar = cocuklar

    def __str__(self,seviye=0):
        sonuc = " " * seviye + str(self.veri)
        for cocuk in self.cocuklar:
            sonuc +=  cocuk.__str__(seviye + 1)

        return sonuc
    
    def cocukekle(self,TreeNode):
        self.cocuklar.append(TreeNode)


D1 = TreeNode("D1",[])
D2 = TreeNode("D2",[])
D3 = TreeNode("D3",[])
D4 = TreeNode("D4",[])
D5 = TreeNode("D5",[])
D6 = TreeNode("D6",[])
D7 = TreeNode("D7",[])
D8 = TreeNode("D8",[])

D1.cocukekle(D2)
D1.cocukekle(D3)

D2.cocukekle(D4)
D2.cocukekle(D5)

D3.cocukekle(D6)

D4.cocukekle(D7)
D4.cocukekle(D8)