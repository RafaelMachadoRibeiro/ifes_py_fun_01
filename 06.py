#Função 1
def pot(a,b):
    resultado = 0
    resultado = a ** b
    return resultado


#Programa principal
x = float(input('Digite o valor de X: '))
y = float(input('Digite o valor de Y: '))
result = pot(x,y)
print('A exponenciação de {} elevado à {} é igual: {} '.format(x,y,result))