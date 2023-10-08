
n = int(input()) 

for i in range(n): 
    comida = float(input()) 
    d = 0 

    while comida > 1: 
        comida = comida / 2 
        d += 1 
    print("{} dias".format(d)) 
