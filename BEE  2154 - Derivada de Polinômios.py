# -*- coding: utf-8 -*-
while True:
    try:
        n = int(input())
    except EOFError:
        break
    saida = ""
    linha = input().split(" + ")

    for j in range(n-1):
        linha_nova = linha[j].split("x")
        multiplicacao = int(linha_nova[0])*int(linha_nova[1])
        expoente = int(linha_nova[1])-1
        if (expoente != 1):
            saida += str(multiplicacao)+"x"+str(expoente)
        else:
            saida += str(multiplicacao)+"x"
        saida += " + "
    linha_nova = linha[n-1].split("x")
    multiplicacao = int(linha_nova[0])*int(linha_nova[1])
    expoente = int(linha_nova[1])-1
    if (expoente != 1):
        saida += str(multiplicacao)+"x"+str(expoente)
    else:
        saida += str(multiplicacao)+"x"
    print(saida)
