
while True:
 
    nt = input().split()
    n_temp = int(nt[0])
    tempo_cap = int(nt[1])

    if n_temp == -1 and tempo_cap == -1:
        break

    lista = input().split()

    acum_temp_anter = 0

    total = 0

    for i in range(n_temp):
     
        acum_temp_anter += int(lista[i]) * tempo_cap
    
        total += acum_temp_anter
   
    print(total)
