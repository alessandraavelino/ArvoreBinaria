class Vertice:
     
    def __init__(self, key, payload):
        self.key = int(key)
        
        self.right = None
        self.left = None
        self.pai = None
        self.payload = payload

    def __str__(self):
        return str(self.key)+" "+str(self.payload)

class Tree:

    def __init__(self):
        self.raiz = None
        self.count = 0

#TREE INSERT
    def treeInsert(self,z):
        y = None 
        x = self.raiz

        while(x != None): #enquanto a raíz for diferente de none
            y = x # none recebe a raíz
            if(z.key < x.key): 
                x = x.left # raíz recebe a esquerda
            else:
                x = x.right #raiz recebe a folha da direita

        z.pai = y
        if(y == None): #se o pai for none,a raíz recebe o 
            self.raiz = z
        elif(z.key < y.key):
            y.left = z
        else:
            y.right = z
        self.count += 1

#TREE SEARCH
    def iterative_tree_search(self, key):
        if(self.raiz == None):
            return None

        vertice = self.raiz
        while(vertice != None and vertice.key != int(key)):
            if(int(key) < vertice.key):
                vertice = vertice.left
            else:
                vertice = vertice.right
        return vertice

#TREE IN ORDER
    def inorder_tree_walk(self, vertice=None):

        if(self.raiz == None):
            return
        if(vertice == None):
            vertice = self.raiz
        if(vertice.left != None):
            self.inorder_tree_walk(vertice = vertice.left)
        print(vertice)
        if(vertice.right != None):
            self.inorder_tree_walk(vertice = vertice.right)

#TREE PRINT DECRESCENTE
    def tree_decrescente(self, vertice=None):

        if(self.raiz == None):
            return
        if(vertice == None):
            vertice = self.raiz
        if(vertice.right != None):
            self.tree_decrescente(vertice = vertice.right)
        print(vertice)
        if(vertice.left != None):
            self.tree_decrescente(vertice = vertice.left)

#TREE PRÉ ORDER
    def preOrder_Tree(self,vertice = None):

        if(self.raiz == None):
            return
        if(vertice == None):
            vertice = self.raiz
        print(vertice)
        if(vertice.left != None):
            self.preOrder_Tree(vertice = vertice.left)
        if(vertice.right != None):
            self.preOrder_Tree(vertice = vertice.right)
               


#TREE PÓS ORDER
    def posOrder_Tree(self,vertice = None):

        if(self.raiz == None):
            return
        if(vertice == None):
            vertice = self.raiz
        if(vertice.left != None):
            self.posOrder_Tree(vertice = vertice.left)
        if(vertice.right != None):
            self.posOrder_Tree(vertice = vertice.right)
        print(vertice)
           

#TREE PREDECESSOR
    def tree_predecessor(self,vertice):
        if(vertice.left != None):
            return self.tree_maximum(vertice=vertice.left)

#TREE MINIMUM RECURSIVO

    def tree_minimum_recursivo(self, vertice = None):
        if(self.raiz == None):
            return None
        if(vertice == None):
            vertice = self.raiz
        while(vertice.left != None):
            vertice = vertice.left
        return vertice
#TREE MAXIMUM
    def tree_maximum(self, vertice = None):
        if(self.raiz == None): #arvore vazia
            return None

        if(vertice == None):
            vertice = self.raiz
    
        while(vertice.right != None):
         vertice = vertice.right
        return vertice


#TREE SUCESSOR
    def tree_sucessor(self,vertice):
        if(vertice.right != None):
            return self.tree_minimum_recursivo(vertice = vertice.right)

        y = vertice.pai
        while(y != None and vertice == y.right):
            vertice = y
            y = vertice.pai

            return y

#TREE TRANSPLANT
    def tree_transplant(self, u, v):
        if(u.pai == None):
            self.raiz = v
        elif(u.pai.left == u):
            u.pai.left = v
        else:
            u.pai.right = v
        if(v != None):
            v.pai = u.pai

#TREE REMOVE
    def tree_Remove(self,z):
        if(z.left == None):
            self.tree_transplant(z,z.right)
        elif(z.right == None):
            self.tree_transplant(z,z.left)
        else:
            y = self.tree_maximum(z.right)

            if(y.pai != z):
                self.tree_transplant(y,y.right)
                y.right = z.right
                y.right.pai = y

            self.tree_transplant(z,y)
            y.left = z.left
            y.left.pai = y

   
     
#### fim da classe ####


def menu():
    print("---> Aluna: Alessandra Avelino - TSI (P2) <---")
    print("---------> Árvore Binária de Busca <----------")
    print("Escolha a opção desejada:")
    print("0 - Sair do programa")
    print("1 - Insert")
    print("2 - Remove")
    print("3 - Search")
    print("4 - In Order")
    print("5 - Pre Order")
    print("6 - Pos Order")
    print("7 - Tree Mínimo")
    print("8 - Tree Máximo")
    print("9 - Decrescente")

    return int(input())

def adicionaVertice(arvore):
    print('Informe o par "key payload"')
    texto = input()
    key, payload = texto.split()
    vertice = Vertice(key, payload)
    arvore.treeInsert(vertice)

def removeVertice(arvore):
    print("Informe a chave de busca ", end="")
    chave = int(input())
    vertice = arvore.iterative_tree_search(chave)
    if(vertice == None):
        print("Vértice de chave ", chave, "não existe")
    else:
        arvore.tree_Remove(vertice)
        print("Vértice removida")
        
def buscaVertice(arvore):
    print("Qual chave você deseja localizar? ", end="")
    chave = int(input())
    vertice = arvore.iterative_tree_search(chave)
    if(vertice == None):
        print("Chave não localizada!")
    else:
        arvore.iterative_tree_search(chave)
        print("Chave", chave, "localizada!")

def main():
    arvore = Tree()
    opcao = menu()
    while(opcao != 0):
        if  (opcao == 1):
            adicionaVertice(arvore)
        elif(opcao == 2):
            removeVertice(arvore)
        elif(opcao == 3):
            buscaVertice(arvore)
        elif(opcao == 4):
            arvore.inorder_tree_walk()
        elif(opcao == 5):
            arvore.preOrder_Tree()
        elif(opcao == 6):
            arvore.posOrder_Tree()
        elif(opcao == 7):
            print(arvore.tree_minimum_recursivo())
        elif(opcao == 8):
            print(arvore.tree_maximum())
        elif(opcao == 9):
            arvore.tree_decrescente()
        else:
            print("Opção inválida!")
        opcao = menu()

if(__name__== "__main__"):
    main()