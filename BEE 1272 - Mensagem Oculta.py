n = int(input())  

for c in range(n):
    palavras = input().split() 
    cont = len(palavras)  
    for i in range(cont):  
        print(palavras[i][0], end='') 
    print()                          
