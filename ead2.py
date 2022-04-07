'''
Felipe da Silva Prado
RGA: 2016.1905.060-9
Funções Implementadas
ERD = Imprime Arvore em-Ordem (Esquerda, Raiz, Direita) e Balanço do respectivo nó
altura = Calcula Altura do Nó   -   tempo O(h) onde h é altura da arvore
balancear = Calcula o balando dos nós    -   tempo O(h) onde h é altura da arvore
insereSemRotacao = insere um nó "x"(se x não estiver na arvore) em uma arvore enraizada por "p" -   tempo O(h) onde h é altura da arvore
busca = verifica se um noh está na arvore ou não -   tempo O(h) onde h é altura da arvore
sucessor = busca o nó folha que é sucessor de um outro nó - tempo O(h) onde h é altura da arvore
BuscaERemoveSemRotacao = remove um elemento da arvore e atualiza  - tempo O(h) onde h é altura da arvore
RD = Faz um rotação a direita sobre um nó - tempo O(h)
RE = Faz um rotação a esquerda sobre um nó - tempo O(h)
DRD = Faz uma dupla Rotação a direita sobre um nó - tempo O(h)

Main
A entrada do programa deve ser dado a quatidade de casos testes em seguida os valores a serem inseridos na Arvore, EX:
1
6 7 8 9 1 2 3
após isso será impresso o resultado

Para testar as demais funções como Remoção e Rotação basta tirar o # que comenta o códio de chamada das funções

'''

def erd(x):
    if(x != None):
        erd(x.esq)
        print(x.info,"(%d)"%x.b,end=" ")        
        erd(x.dir)
    
def altura(p):
    if p == None:
        return 0
    hesq = altura(p.esq)
    hdir = altura(p.dir)
    if hesq >= hdir:
        hesq = hesq + 1
        return hesq
    else:
        hdir = hdir + 1
        return hdir
def balancear(p):
    while p != None:
        #print("Noh Info: ",p.info)
        p.b = altura(p.esq) - altura(p.dir)
        if(p.pai == None):    
            break
        else:
            p = p.pai        

def insereSemRotacao (p, x):
    novo = x
    if p == None:
        p = novo
        return p
    else:
        if( busca(p,x.info)!= None):
            return p
        else:
            atual = p
            while True:
                anterior = atual
                if x.info <= atual.info: #vai pra esquerda
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = novo
                        anterior.esq.pai = anterior
                        #print("Inseriu a Esquerda: ",anterior.esq.info)
                        balancear(anterior)
                        break 
                else: #vai para dir
                    atual = atual.dir
                    if atual == None:
                        anterior.dir = novo
                        anterior.dir.pai = anterior
                        #print("Inseriu a Direita: ",anterior.dir.info)
                        balancear(anterior)
                        break        
            return p
def busca(p , x):
    #print("Entrou na Busca pelo",x)
    if p == None:
        print("Arvore Vazia")
        return None
    else:
        atual = p
        while x != atual.info:
            if x < atual.info:
                atual = atual.esq
            else:
                atual = atual.dir
            if atual == None:
                #print("Não Achou")
                return None
        #print("Achou",atual.info)
        return atual    

def sucessor(p):
    atual = p
    while atual != None :
        aux = atual
        if(atual.esq != None):
            atual = atual.esq
        else:
            atual = atual.dir
    print("Sucessor: ",aux.info)
    return aux

def BuscaERemoveSemRotacao(p , x):
    noh = busca(p,x)
    if noh == None:
        return None
    else:
        if (noh.esq == None) and (noh.dir == None): #é folha
            print("É Folha:")
            #verificar se ele é filho esquerdo ou direito para atualizar
            if(noh.pai.esq == noh):
                noh.pai.esq = None
            else:
                noh.pai.dir = None
            auxb = noh.pai
            noh = None
            balancear(auxb)
            return p
        elif(noh.dir == None ): #possui filho a esquerda
            print("Filho ESQ:")
            suc = sucessor(noh.esq)
            noh.info = suc.info
            #arrumar pai do sucessor
            auxb = suc.pai
            if(auxb.esq == suc): 
                suc.pai.esq = None
            else:
                suc.pai.dir = None
            suc = None
            balancear(auxb)
            return p
        elif(noh.esq == None ): #possui filho a direita
            print("Filho DIR:")
            suc = sucessor(noh.dir)
            noh.info = suc.info
            auxb = suc.pai
            if(auxb.esq == suc): 
                suc.pai.esq = None
            else:
                suc.pai.dir = None
            suc = None
            balancear(auxb)
            return p
        else: #possui os 2 filhos
            print("Filho ESQ E DIR:")
            suc = sucessor(noh.dir)
            noh.info = suc.info
            auxb = suc.pai
            if(auxb.esq == suc): 
                suc.pai.esq = None
            else:
                suc.pai.dir = None
            suc = None
            balancear(auxb)
            
            return p

def RD(p):
    #print("RD")
    x = p.esq
    x.pai = p.pai
    T2 = x.dir
    x.dir = p
    p.esq = T2
    if T2 != None:
        T2.pai = p
    p.pai = x
    
    balancear(x)
    balancear(p)
    return x

def RE(p):
    #print("RE")
    y = p.dir
    y.pai = p.pai 
    T2 = y.esq
    y.esq = p
    p.dir = T2

    if T2 != None:
        T2.pai = p
    p.pai = y
 
    balancear(y)
    balancear(p)
    return y

def DRD(p):
    x = RE(p.esq)
    p.esq = x
    y = RD(p)
    return y

class No:
    # os atributos de No sao:
    #        info
    #        pai
    #        esq
    #        dir
    #        b
    
    def __init__ (self, info):
        self.info = info
        self.pai = self.dir = self.esq = None
        self.b = 0
'''MAIN'''
n = int(input())
for i in range(n):
    entrada = input().split()
    p = None
    # p inicialmente eh vazia
    for j in range(len(entrada)):
        x = No(int(entrada[j]))        # cria um No x
        p = insereSemRotacao (p, x)  # insere x na arvore enraizada por T
    erd(p)
    print()
    #y = int(input("Digite um nó a ser encontrado e Removido: "))
    #p = BuscaERemoveSemRotacao(p,y)
    #erd(p)
    #print()
    #print("Rotacao a direita")
    #p = RD(p)
    #print()
    #print("Dupla Rotacao a direita")
    #p = DRD(p)
    #erd(p)
    #print()
    
