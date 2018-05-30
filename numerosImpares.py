'''
Receba um número inteiro positivo na entrada e imprima os n
primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.
'''

n = int(input('Digite o valor de n: '))
impar = 1
while n != 0:
    print (impar)
    n = n - 1
    impar = impar + 2
