#Ventiladores de baloÊs
while True:
    string = input().split()
    L = int(string[0])
    C = int(string[1])
    P = int(string[2])
    if (L == 0 and C == 0 and P == 0):
        break

    caixa = [] 
    for i in range(L):
        linha = input().split() 
        lst = []
        for j in range(C): 
            lst.append(int(linha[j])) 
        caixa.append(lst)

    balao = P - 1 
    
    
    i = 0         
    boom = False 
    while not boom and i <= L - 1:
        
        for j in range (balao, -1, -1):
            if (caixa[i][j] > 0):
                ventEsq = j
                potEsq = caixa[i][j]
                break
            
        for k in range (balao, C):
            if (caixa[i][k] > 0):
                ventDir = k
                potDir = caixa[i][k]
                break

        dif = potEsq - potDir 
        if dif < 0: 
         
            if (balao + dif <= ventEsq):
                boom = True
                balao = ventEsq
            else:
                balao = balao + dif
        elif dif > 0:
                      
            if (balao + dif >= ventDir):
                boom = True
                balao = ventDir
            else:
                balao = balao + dif    
        i = i + 1 
  
    if boom == True:
        print("BOOM", str(i), str(balao+1))
    else:           
        print("OUT", str(balao+1))
                
