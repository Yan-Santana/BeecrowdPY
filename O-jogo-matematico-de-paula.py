n = int(input())

for c in range(n):
    lst = input()

    numero1 = int(lst[0])
    letra = lst[1]
    numero2 = int(lst[2])

    if numero1 == numero2:
        produto = numero1 * numero2
        print(produto)

    elif letra.isupper():
        sub = numero2 - numero1
        print(sub)
    else:
        soma = numero1 + numero2
        print(soma)
        