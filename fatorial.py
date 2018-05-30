'''
Escreva um programa que receba um número natural n n na entrada e imprima n! n! (fatorial) na saída. usando while
'''

n = int(input('Digite o valor de n: '))
soma = 1
while n != 1:
    soma = soma * n
    n = n - 1

print(soma)
