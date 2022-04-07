'''
Felipe da Silva Prado RGA: 2016.1905.060-9
'''

def forcaBruta(t, p):
    print("Força Bruta")
    n = len(t)
    m = len(p)
    k = 0
    Comparacoes = 0
    for i in range(n-m+1):
        j = 0
        
        while j < m and p[j] ==  t[i+j]:
            j+=1
            Comparacoes+=1
        if j == m:
            k+=1
            #print("Encontrado em T[",i+1,"]")
        else:
            Comparacoes+=1
    return print("Ocorrências: ",k," | Comparações: ",Comparacoes)    

def prefixo( p):

    vet = [0]
    
    for i in range(1, len(p)):
        j = vet[i - 1]
        while j > 0 and p[j] != p[i]:
            j = vet[j - 1]
        vet.append(j + 1 if p[j] == p[i] else j)
    return vet
    
def kmp(t, p):
    print("KMP")
    pref = prefixo(p)
    vet = []

    j = 0
    aux = 0
    Comparacoes = 0
    for i in range(len(t)):
        while j > 0 and t[i] != p[j]:
            j = pref[j - 1]
            Comparacoes+=1
        if t[i] == p[j]: 
            j += 1 
            Comparacoes+=1
        if j == len(p): 
            
            aux +=1
            vet.append(i - (j - 1))
            j = pref[j - 1]
        
    return print("Ocorrências: ",aux," | Comparações: ",Comparacoes)


###MAIN###
t = input("Digite o Texto: ")
p = input("Digite a Palavra: ")
forcaBruta(t, p)
kmp(t,p)
