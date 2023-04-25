#Função 1
def potencia(a,b):
    soma = 1
    for i in range(b):
        soma = soma * a
    return soma

#Programa principal
x = int(input('Digite o valor de X: '))
y = int(input('Digite o valor de Y: '))
result = potencia(x,y)
print('O resultado de {} elevado à {} é igual à: {}'.format(x,y,result))