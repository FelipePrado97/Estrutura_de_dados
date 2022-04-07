'''
EAD1 - ESTRUTURA DE DADOS 
FELIPE DA SILVA PRADO  | RGA: 2016.1905.060-9
PROF: FRANCISCO ELÓI

'''

class No:
    def __init__(self, info, dir, esq, pai):
        self.info = info
        self.dir = dir
        self.esq = esq
        self.pai = pai
    
def erd(atual):
    if(atual != None):
        erd(atual.esq)
        print(atual.info, end=" ")
        erd(atual.dir)

def red(atual):
    if(atual != None):
        print(atual.info, end=" ")
        red(atual.esq)
        red(atual.dir)

def edr(atual):
    if(atual != None):
        edr(atual.esq)
        edr(atual.dir)
        print(atual.info, end=" ")


def imprime(raiz):
    print("Pre ordem (RED): ",end="")
    red(raiz)
    
    print("\nIn ordem   (ERD): ",end="")
    erd(raiz)

    print("\nPos ordem (EDR): ",end="")
    edr(raiz)

def posicao(raiz,l_erd):
        j = 0
        while l_erd[j] != raiz:
            j+=1
        return j

def AB(l_red, l_erd):
    print("RED and ERD: ",l_red,l_erd)
    nova = No(None,None,None,None)
        
    n = len(l_red)
    if n == 0:
        if len(l_erd) != 0:
            print("INSERIU: ",l_erd)
            atual = nova
            atual.info = l_erd[0]
            return atual
        return None
    atual = nova
    
    j = posicao(l_red[0],l_erd)
    print("Pivo:",j,l_erd[j])
    esq = l_erd[0:j]
    dir = l_erd[j+1:n+1]
    print("Esquerda e Direita: ",esq, dir)
    e = AB(l_red[1:j],esq)
    d = AB(l_red[j+1:n],dir)
    atual.info = l_red[0]
    print("INSERIU: ",atual.info, atual.dir, atual.esq,atual.pai)
    atual.esq = e
    atual.dir = d
    if atual.esq == None and atual.dir != None: #so tem filho a direita
        atual.dir.pai = atual
        print("pai d: ",atual.dir.pai)
    if atual.esq != None and atual.dir == None: #so tem filho a esq
        atual.esq.pai = atual
        print("pai e: ",atual.esq.pai)
    if atual.esq != None and atual.dir != None: #tem 2 filhos
        atual.esq.pai = atual
        atual.dir.pai = atual
        print("pai d: ",atual.dir.pai)
        print("pai e: ",atual.esq.pai)
    return nova

def pai(raiz,letra):
    
    if(raiz != None):
        print("NO: ",raiz.info,"Pai dele: ", raiz.pai,"Endereço dele: ", raiz)
        pai(raiz.esq,letra)
        pai(raiz.dir,letra)
        
    



### MAIN() ###

lista_red = []
lista_erd = []
lista_red = input("Entre com a lista RED: ")

lista_erd = input("Entre com a lista ERD: ")

print()

x = AB(lista_red, lista_erd)
pai(x,lista_red[2])
imprime(x)
