lmsg = input().split()
n = len(lmsg)
vetor = [""]*n

for i in range(n):
    lingua_p = lmsg[i]

    for j in range(1, len(lingua_p), 2):
        vetor[i] += lingua_p[j]
decodificada = ""
for c in  range(0, n-1):
    decodificada += vetor[c] + " "
decodificada += vetor[n -1]
print(decodificada)
