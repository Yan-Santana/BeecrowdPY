# -*- coding: utf-8 -*-
def inteiros(x):
    #Função para converter os indices da lista em inteiros.
    for c in range(len(x)):
        x[c] = int(x[c])
    return x
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

t = int(input()) # representa o número de casos de teste
cont = 0
for c in range(1, t + 1): # vai iniciar um laço do 1 até t+1
    jogadores = input().split() # pegar os membros de cada equipe 
    jogadores = inteiros(jogadores) # vai chamar a função para converter para inteiros 
    cap = (len(jogadores) + 1) // 2 # vai ver quantos indices tem na lista de jogadores e dividir por 2
    capitao = jogadores[cap] # O capitão será o meio termo da quantidade de jogadores
    print("Case {}: {}".format(c, capitao)) #  vai imprimir o "case" e a idade do capitão