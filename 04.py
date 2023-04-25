#1º Função
def multiplicador(a,b):
    result = 0
    result = a * b
    return result

#Programa principal
x = float(input('Digite o valor de X: '))
y = float(input('Digite o valor de Y: '))
result = multiplicador(x,y)
print('O resultado da multiplicação entre {} e {} é igual à: {}'.format(x,y,result))
