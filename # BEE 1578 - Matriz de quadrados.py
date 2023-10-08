# BEE 1578 - Matriz de quadrados

N = int(input()) # Quantidade de matrizes 

for c in range(N): #Laço para saber a dimensaão das matrizes
    dim = int(input()) # dimensão da matriz
    matriz = []
    
    for i in range(dim):
        linha = input().split()
        l_int = []
        for j in range(dim):
            l_int.append(int(linha[j]))
        matriz.append(l_int)
    
    for i in range(dim): # laço para colocar na matriz quadrada
        for j in range(dim):
            matriz[i][j] = matriz[i][j] **2 #Cada valor da matriz elevado ao quadrado
            
    mat_str = [] # Cria uma lista vazia onde será colocados os dados da matriz como string
    for i in range(dim):
        linha = [" "]*dim
        for j in range(dim):
            linha[j] = str(matriz[i][j])
        mat_str.append(linha)
    
    str_max = dim*[0] # variavel para indicar a maior str que tem na coluna
    
    for j in range(dim):
        for i in range(dim):
            len_str = len(mat_str[i][j])
            if len_str > str_max[j]:
                str_max[j] = len_str
    
    esp = ' '
    for j in range(dim):
        for i in range(dim):
            mat_str[i][j] = esp*(str_max[j] - len(mat_str[i][j])) + mat_str[i][j]
    
    print("Quadrado da matriz #{0:d}:".format(4+c))
    for i in range(dim):
        for j in range(dim-1):
            print(mat_str[i][j], "", end="")
        print(mat_str[i][dim-1])
        
    if c < N-1:
        print()

            
