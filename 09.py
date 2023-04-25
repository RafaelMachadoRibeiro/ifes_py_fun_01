#1º função
def fatorial(x):
    k_fat = 1
    for i in range(x,1,-1):
        k_fat=k_fat*i
    return k_fat

#Programa principal
n = int(input('Digite o valor que deseja calcular o fatorial: '))
result = fatorial(n)
print('O valor do fatorial de {} é igual à: {}'.format(n,result))