class Vertice:
     
    def __init__(self, key):
        self.key = (key)
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

class Tree:
    def __init__(self, key = None):
        if key:
            vertice = Vertice(key)
            self.raiz = vertice
        else:
            self.raiz = None
    
    def inorder_Tree_walk(self,vertice = None):
        if(vertice is None):
            vertice = self.raiz
        if(vertice.left != None):
            self.inorder_Tree_walk(vertice.left)
        print(vertice, end="\n")
        if(vertice.right != None):
            self.inorder_Tree_walk(vertice.right)


if __name__ == "__main__":
    #arv = Tree(7)
    #arv.raiz.left = Vertice(18)
    #arv.raiz.right = Vertice(14)

    #print(arv.raiz)
    #print(arv.raiz.right)
    #print(arv.raiz.left)

    arv = Tree()

    n1 = Vertice("a")
    n2 = Vertice("+")
    n3 = Vertice("*")
    n4 = Vertice("b")
    n5 = Vertice("-")
    n6 = Vertice("/")
    n7 = Vertice("c")
    n8 = Vertice("d")
    n9 = Vertice("e")

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    arv.raiz = n2

    arv.inorder_Tree_walk()