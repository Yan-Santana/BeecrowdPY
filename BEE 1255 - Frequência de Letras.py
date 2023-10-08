N = int(input())
for i in range(N):
    contador = [0]*26
    texto = input()
    
    
    for j in range(len(texto)):
        minus = ord(texto[j].lower())
        if minus >= 97 and minus <= 122:
            contador[minus - 97] += 1
    
    
    maiorfreq = -1
    for j in range(26):
        if contador[j] > maiorfreq:
            maiorfreq = contador[j]
        
    
    for j in range(26):
        if (contador[j] == maiorfreq):
            print(chr(j+97), end="")
    print() 
