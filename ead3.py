'''
Felipe da Silva Prado
RGA: 2016.1905.060-9
Funções Implementadas
ERD = Imprime Arvore na Ordem: (Esquerda, Raiz, Direita) e Balanço do respectivo nó
RED = Imprime Arvore na Ordem: (Raiz, Esquerda, Direita)
altura = Calcula Altura do Nó 
balancear = Calcula o balando dos nós    
insereSemRotacao = insere um nó "x"(se x não estiver na arvore) em uma arvore enraizada por "p"
insereAVL = insere um nó "x"(se x não estiver na arvore) em uma arvore enraizada por "p" e rotaciona atualizando o balanço dos nós
busca = verifica se um nó está na arvore ou não 
sucessor = busca o nó folha que é sucessor de um outro nó
BuscaERemoveSemRotacao = remove um elemento "x"(se x estiver na arvore) da arvore e atualiza o balanço dos nós
BuscaERemoveAVL = remove um elemento "x"(se x estiver na arvore) da arvore, rotaciona(caso necessário) e atualiza o balanço dos nós
rotacao = rotaciona um nó se o mesmo está desbalanceado, e aplica a rotação correta sobre ele
RD = Faz um rotação a direita sobre um nó 
RE = Faz um rotação a esquerda sobre um nó 
DRD = Faz uma dupla Rotação a direita sobre um nó
DRE = Faz uma dupla Rotação a esquerda sobre um nó
'''

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

def BuscaERemoveSemRotacao(p , x):
    noh = busca(p,x)
    if noh == None:
        return None
    else:
        if (noh.esq == None) and (noh.dir == None): #é folha
            #print("É Folha:")
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
            #print("Filho ESQ:")
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
            #print("Filho DIR:")
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
            #print("Filho ESQ E DIR:")
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

def erd(x):
    if(x != None):
        erd(x.esq)
        print(x.info,"(%d)"%x.b,end=" ")        
        erd(x.dir)

def red(x):
    if(x != None):
        print(x.info,end=" ")
        red(x.esq)        
        red(x.dir)
    
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

def insereAVL(p,x):
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
                                            
                        while anterior != None:
                            if(anterior.b==2 or anterior.b==-2):
                                #print("Noh disbalanceado ",anterior.info)
                                if anterior.pai == None: #se é raiz
                                    p = rotacao(anterior)
                                else: #pode ser filho direito ou filho esquerdo
                                    aux = anterior.pai
                                    #print("pai do disbalanceado ", aux.info)
                                    if aux.esq == anterior: #Filho esquerdo
                                        anterior = rotacao(anterior) 
                                        #print("raiz da nova rotação ", anterior.info)
                                        aux.esq = anterior
                                        balancear(aux)
                                        aux = aux.pai 
                                        anterior = aux
                                    else: #filho deito
                                        anterior = rotacao(anterior)
                                        #print("raiz da nova rotação ", anterior.info)
                                        aux.dir = anterior
                                        balancear(aux)
                                        aux = aux.pai
                                        anterior = aux 
                            else:
                                anterior = anterior.pai
                        break 
                else: #vai para dir
                    atual = atual.dir
                    if atual == None:
                        anterior.dir = novo
                        anterior.dir.pai = anterior
                        #print("Inseriu a Direita: ",anterior.dir.info)
                        balancear(anterior)
                        
                        while anterior != None:
                            if(anterior.b==2 or anterior.b==-2):
                                #print("Noh disbalanceado ",anterior.info)
                                if anterior.pai == None: #se é raiz
                                    p = rotacao(anterior)
                                else: #pode ser filho direito ou filho esquerdo
                                    aux = anterior.pai
                                    #print("pai do disbalanceado ", aux.info)
                                    if aux.esq == anterior: #Filho esquerdo
                                        anterior = rotacao(anterior) 
                                        #print("raiz da nova rotação ", anterior.info)
                                        aux.esq = anterior
                                        balancear(aux)
                                        aux = aux.pai 
                                        anterior = aux
                                    else: #filho deito
                                        anterior = rotacao(anterior)
                                        #print("raiz da nova rotação ", anterior.info)
                                        aux.dir = anterior
                                        balancear(aux)
                                        aux = aux.pai
                                        anterior = aux 
                            else:
                                anterior = anterior.pai
                        break        
            return p    

def BuscaERemoveAVL(p , x):
    noh = busca(p,x)
    if noh == None:
        return None
    else:
        if (noh.esq == None) and (noh.dir == None): #é folha
            #print("É Folha:")
            #verificar se ele é filho esquerdo ou direito para atualizar
            if(noh.pai.esq == noh):
                noh.pai.esq = None
            else:
                noh.pai.dir = None
            auxb = noh.pai
            noh = None
            balancear(auxb)
            while(auxb != None):
                if(auxb.b==2 or auxb.b==-2):
                    if auxb.pai == None:
                        p = rotacao(auxb)
                    else: #pode ser filho direito ou esquerdo
                        aux = auxb.pai
                        if auxb.pai.esq == auxb: #filho esquerdo
                            auxb = rotacao(auxb)
                            aux.esq = auxb
                            balancear(aux)
                            aux = aux.pai
                            auxb = aux
                        else: #filho direito
                            auxb = rotacao(auxb)
                            aux.dir = auxb
                            balancear(aux)
                            aux = aux.pai
                            auxb = aux
                else:
                    auxb = auxb.pai
            #auxiliarRemocao(auxb)
            return p
        elif(noh.dir == None ): #possui filho a esquerda
            #print("Filho ESQ:")
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
            while(auxb != None):
                if(auxb.b==2 or auxb.b==-2):
                    if auxb.pai == None:
                        p = rotacao(auxb)
                    else: #pode ser filho direito ou esquerdo
                        aux = auxb.pai
                        if auxb.pai.esq == auxb: #filho esquerdo
                            auxb = rotacao(auxb)
                            aux.esq = auxb
                            balancear(aux)
                            aux = aux.pai
                            auxb = aux
                        else: #filho direito
                            auxb = rotacao(auxb)
                            aux.dir = auxb
                            balancear(aux)
                            aux = aux.pai
                            auxb = aux
                else:
                    auxb = auxb.pai
            return p
        elif(noh.esq == None ): #possui filho a direita
            #print("Filho DIR:")
            suc = sucessor(noh.dir)
            noh.info = suc.info
            auxb = suc.pai
            if(auxb.esq == suc): 
                suc.pai.esq = None
            else:
                suc.pai.dir = None
            suc = None
            balancear(auxb)
            while(auxb != None):
                if(auxb.b==2 or auxb.b==-2):
                    if auxb.pai == None:
                        p = rotacao(auxb)
                    else: #pode ser filho direito ou esquerdo
                        aux = auxb.pai
                        if auxb.pai.esq == auxb: #filho esquerdo
                            auxb = rotacao(auxb)
                            aux.esq = auxb
                            balancear(aux)
                            aux = aux.pai
                            auxb = aux
                        else: #filho direito
                            auxb = rotacao(auxb)
                            aux.dir = auxb
                            balancear(aux)
                            aux = aux.pai
                            auxb = aux
                else:
                    auxb = auxb.pai
            return p
        else: #possui os 2 filhos
            #print("Filho ESQ E DIR:")
            suc = sucessor(noh.dir)
            noh.info = suc.info
            auxb = suc.pai
            if(auxb.esq == suc): 
                suc.pai.esq = None
            else:
                suc.pai.dir = None
            suc = None
            balancear(auxb)
            while(auxb != None):
                if(auxb.b==2 or auxb.b==-2):
                    if auxb.pai == None:
                        p = rotacao(auxb)
                    else: #pode ser filho direito ou esquerdo
                        aux = auxb.pai
                        if auxb.pai.esq == auxb: #filho esquerdo
                            auxb = rotacao(auxb)
                            aux.esq = auxb
                            balancear(aux)
                            aux = aux.pai
                            auxb = aux
                        else: #filho direito
                            auxb = rotacao(auxb)
                            aux.dir = auxb
                            balancear(aux)
                            aux = aux.pai
                            auxb = aux
                else:
                    auxb = auxb.pai
            return p

def busca(p , x):
    #print("Entrou na Busca pelo",x)
    if p == None:
        #print("Arvore Vazia")
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
    #print("Sucessor: ",aux.info)
    return aux

def rotacao(p):
    if p.b == 2 and p.esq.b >= 0: #rotacao a direita
        #print("Rotacao a direita")
        return RD(p)
    elif p.b == -2 and p.dir.b <= 0: #rotacao a esquerda
        #print("Rotacao a esquerda")
        return RE(p)
    elif p.b == 2 and p.esq.b == -1: #Dupla Rotacao a direita
        #print("Dupla Rotacao a direita")
        return DRD(p)
    elif p.b == -2 and p.dir.b == 1: #Dupla Rotacao a esqerda 
        #print("Dupla Rotacao a esqerda")
        return DRE(p)
    else:
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

def DRE(p):
    x = RD(p.dir)
    p.dir = x
    y = RE(p)
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
        #p = insereSemRotacao(p, x)
        p = insereAVL(p, x)  # insere x na arvore enraizada por T
    print()
    erd(p)
    print()
    red(p)
    print()
    y = int(input("Digite o nó a ser encontrado: "))
    #p = BuscaERemoveSemRotacao(p,y)
    p = BuscaERemoveAVL(p,y)
    print()
    erd(p)
    print()
    red(p)
    print()
