#1º função
def fatorial_n(n):
    calc_n = 1
    for i in range(n,1,-1):
        calc_n = calc_n * i
    return calc_n

#2º função
def result_arranjo(n,p):
    if(n<p):
        return -1
    else:
        return fat_n/fat_np 

#Programa principal
n = int(input('Digite o valor de n: '))
p = int(input('Digite o vlaor de p: '))

fat_n = fatorial_n(n)
fat_np = fatorial_n(n-p)
fat_res = result_arranjo(fat_n,fat_np)

print('O resultado do arranjo que o valor de N é {} P é {}, o resultado é igual: {}'.format(n,p,fat_res))