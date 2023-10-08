import math
def fatmaior(n, exp):
    if n == 0 or n == 1:
        if (exp > 1):
            return True
    else:
        if n >= 6:
            if n >= math.log(exp)/math.log(n/3):
                return True
            if n <= math.log(exp)/math.log(n/2):
                return False
        total = 1
        for i in range(n, 1, -1):
            total *= i
        if total > exp:
            return True
    return False


n = int(input())

vencedor = n*[""]
V_Lucas = 0
V_Pedro = 0

for i in range(n):
    lexp = input().split("^") # Lucas
    lfat = input() # Pedro
    exp = int(lexp[0]) ** int(lexp[1])
    maior = fatmaior(int(lfat[:len(lfat)-1]), exp)
    if (maior):
        vencedor[i] = "Pedro"
        V_Pedro += 1
    else:
        vencedor[i] = "Lucas"
        V_Lucas += 1

if V_Lucas == V_Pedro:
    print("A competicao terminou empatada!")
elif V_Lucas > V_Pedro:
    print("Campeao: Lucas!")
else:
    print("Campeao: Pedro!")

for i in range(n):
    print("Rodada #{0:d}: {1:s} foi o vencedor".format(i+1, vencedor[i]))
