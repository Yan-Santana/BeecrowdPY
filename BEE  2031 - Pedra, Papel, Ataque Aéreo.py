n = int(input())  

for i in range(n):  
    jogador1 = input() 
    jogador2 = input() 

   
    if jogador1 == "ataque":  
        if jogador2 == "ataque":
            print("Aniquilacao mutua")  

        elif jogador2 == "pedra":  
            print("Jogador 1 venceu") 

        else: 
            print("Jogador 1 venceu")

    if jogador1 == "pedra":  
        if jogador2 == "ataque": 
            print("Jogador 2 venceu") 
        elif jogador2 == "pedra": 
            print("Sem ganhador")  
        else:
            print("Jogador 1 venceu")

    if jogador1 == "papel":  # Se o jogador 1 escolher "papel"
        if jogador2 == "ataque": 
            print("Jogador 2 venceu")
        elif jogador2 == "pedra": 
            print("Jogador 2 venceu")  
        else:
            print("Ambos venceram")  
           
