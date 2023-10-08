M = []
for i in range(4):
    lin = input()
    M.append(list(lin))
    
N = len(M[0]) - 2

Fs = ""
Ls = ""
lmsg = N * [""]

for i in range(4):
    Fs += M[i][0]
    Ls += M[i][N+1]
    for j in range(N):
        lmsg[j] += M[i][j+1]

F = int(Fs)
L = int(Ls)

saida = ""
for i in range(N):
    saida += chr((F*int(lmsg[i])+L) % 257)
print(saida)
