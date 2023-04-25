#1º função
def primo(x):
    if x%2>0 and x%3>0 and x%5>0 and x%11>0:
        return True
    else:
        return False

#Programa principal
x = int(input('Digite o valor de X (positivo): '))
result = primo(x)
print ('O número {} quando é verificado se é primo ou não o resultado é: {}'.format(x,result))