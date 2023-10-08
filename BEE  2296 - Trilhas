N = int(input())
id_mais_facil = -1
percurso_mais_facil = 999*1000+1
for n_trilha in range(1, N+1):
    trilha = input().split()
    M = int(trilha[0])
    pontos = [0]*M
    
    for i in range(1, M+1):
        pontos[i-1] = int(trilha[i])
    
    ida = 0
    volta = 0
    for p in range(1, M):
        esq_dir = pontos[p] - pontos[p-1]

        if (esq_dir > 0):
            ida += esq_dir
      
        dir_esq = pontos[p-1] - pontos[p]

        if (dir_esq > 0):
            volta += dir_esq
    
    if (ida < percurso_mais_facil):
        id_mais_facil = n_trilha
        percurso_mais_facil = ida
    if (volta < percurso_mais_facil):
        id_mais_facil = n_trilha
        percurso_mais_facil = volta
print(id_mais_facil)
