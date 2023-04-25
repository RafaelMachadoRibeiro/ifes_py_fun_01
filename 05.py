#1º função
def multiplicador (a,b):
    mult = 0
    for i in range(a):
        mult = mult + b
    return mult

#Programa principal
x = int(input('Digite o valor de X: '))
y = int(input('Digite o valor de Y: '))
result = multiplicador(x,y)
print('O resultado da multiplicação entre {} e {} é igual à: {}'.format(x,y,result))