# -*- coding: utf-8 -*-

lst_matriz = []

lin = int(input())

op = input()


soma = 0.0

for i in range(12):
    
    lst_linha = []
    
    for j in range(12):

        lst_linha.append(float(input()))
    
    lst_matriz.append(lst_linha)

for j in range(12):
    soma += lst_matriz[lin][j]
    
if op == 'S':
    print("{0:.1f}".format(soma))
else:
    print("{0:.1f}".format(soma/12))



