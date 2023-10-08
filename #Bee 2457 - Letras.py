#Bee 2457 - Letras

letra = input()
palavra = input().split()
tamanho = len(palavra)
porc_palavras = 0

for c in range(tamanho):
    if letra in palavra[c]:
        porc_palavras += 1

porc_palavras = porc_palavras / (tamanho / 100)

print("{:.1f}".format(porc_palavras))
