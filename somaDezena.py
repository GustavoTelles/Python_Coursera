

n1 = int(input('Digite um número: '))
soma = 0
total = 0
while n1 != 0:
    soma = int(n1 % 10)
    total = soma + total
    n1 = n1 / 10

print('A soma dos números é  {}' .format(int(total)))
