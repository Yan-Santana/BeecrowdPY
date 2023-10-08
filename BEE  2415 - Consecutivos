# contém um inteiro "n". Número de valores sorteados.
n = int(input())
# Valores na ordem de sorteio, seprados por espaço.
val = input().split()
# contador para contar os pontos 
cont = 1
# sequencia 
seq = 1
# loop para achar os iguais
for c in range(1, n):
    # se valor contido no indice[c] é igual ao anterios[c - 1]
    if val[c] == val[c - 1]:
        # sequencia += 1
        seq += 1
    # senão
    else:
        # se 1 é maior que o contador 
        if seq > cont:
            # Contador recebe a sequencia
            cont = seq
        # reseta a sequencia
        seq = 1
# Se a sequencia for maior que o contador então:
if seq > cont:
    # contador recebe a sequequencia 
    cont = seq
print(cont)
