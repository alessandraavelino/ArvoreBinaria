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

# Insert !
    def treeInsert(self,z):
        y = None 
        x = self.raiz

        while(x != None): 
            y = x 
            if(z.key < x.key): 
                x = x.left 
            else:
                x = x.right 

        z.pai = y
        if(y == None):  
            self.raiz = z
        elif(z.key < y.key):
            y.left = z
        else:
            y.right = z
        self.count += 1
    
    def tree_maximum(self, vertice = None):
        if(self.raiz == None):
            return None

        if(vertice == None):
            vertice = self.raiz
    
        while(vertice.right != None):
         vertice = vertice.right
        return vertice


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
               
    

def menu():
    print("ABB - MENU")
    print("Escolha a opção desejada:")
    print("0 - Sair do programa")
    print("1 - Inserir")
    print("2 - Imprimir decrescente")

    return int(input("-> "))

def adicionaVertice(arvore):
    print('Informe o par "key payload:"')
    texto = input("-> ")
    key, payload = texto.split()
    vertice = Vertice(key, payload)
    arvore.treeInsert(vertice)

def main():
    arvore = Tree()
    opcao = menu()
    while(opcao != 0):
        if (opcao == 1):
            adicionaVertice(arvore)
        elif(opcao == 2):
            print("** Imprimindo em Ordem Decrescente: ***")
            arvore.tree_decrescente()
        else:
            print("Opção inválida!")
        opcao = menu()
        
if(__name__== "__main__"):
    main()
