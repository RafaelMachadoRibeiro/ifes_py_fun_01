#Função para verificar qual é o maior número
def maior(x,y):
    if(x>y):
        return x
    elif(y>x):
        return y

#Programa principal
x = float(input('Digite o valor de X: '))
y = float(input('Digite o valor de Y: '))
print('O maior número entre {} e {}, é o número: {}'.format(x,y,maior(x,y)))