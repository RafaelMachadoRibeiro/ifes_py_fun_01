#Função para verificar se X é par
def inteiro(x):
    if ((x%2)==0):
        return(True)
    else:
        return(False)

#Programa inicial
x = int(input('Digite o valor de X: '))
print(inteiro(x))