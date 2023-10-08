
n = int(input()) # indica o número de casos de teste.

for i in range(n): # Vai perguntar a quantidade de comida 'n' vezes que foi informado.
    comida = float(input()) # 'c' corresponde a quantidade de comida em Kg(float).
    d = 0 # dias, iniciando pelo dia 0.

    while comida > 1: # Enquanto a quantidade de comida informado for maior que 1, que é o restante(1 Kg).
        comida = comida / 2 # pega a metade de comida informado e divide por 2.
        d += 1 # soma um 1, correspondente a um dia que a comida rendeu.
    print("{} dias".format(d)) # vai imprimir a quantidade de dias que a comida vai dar com uma casa decimal. 
