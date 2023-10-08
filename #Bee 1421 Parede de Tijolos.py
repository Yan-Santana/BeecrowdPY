#Bee 1421 Parede de Tijolos
while True:
    try:
        N = int(input())
    except EOFError:
           break
        
    if N == 0:
        break

    matriz = []

    for c in range(N):
        linha = []
        for i in range(N):
            linha.append(1)
        matriz.append(linha)

    val = 1
    superior = 0
    esq = 0
    inferior = N - 1
    Dir = N-1

    if N % 2 == 0:
        meio = N / 2
    else:
        meio = (N+1) / 2

    while val <= meio:
        i = esq
        while i <= Dir:
            matriz[superior][i] = val
            matriz[inferior][i] = val
        i += 1

        i = superior + 1
        while i < inferior:
            matriz[i][esq] = val
            matriz[i][Dir] = val
            i += 1
        
        val += 1
        superior += 1
        inferior += 1
        esq += 1
        Dir -= 1

    for c in range(N):
        text = ''
        for i in range(N):
            text += matriz[c][i]
    print(text[1:])
