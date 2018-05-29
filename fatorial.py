'''
Escreva um programa que receba um número natural n n na entrada e imprima n! n! (fatorial) na saída. usando while
'''

n1 = n = int(input('Digite um numero: '))
soma = 0
while n != 1:
    soma = n1 * (n - 1)
    n1 = soma
    n = n - 1

print('O valor fatorial é: ', soma)
