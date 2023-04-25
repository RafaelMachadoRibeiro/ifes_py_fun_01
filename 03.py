# 1ºfunção
def menor(a,b):
    if a > b:
        return b,a
    else:
        return a,b
# 2º função
def faz_som(x,y):
    soma = 0
    for i in range(x+1, y):
        soma = soma + i
    return (soma)

# Função principal
a = int(input('Digite o valor de A (positivo): '))
b = int(input('Digite o valor de B (positivo): '))
Menor, maior = menor(a,b)
print(f"A soma dos valores entre {a} e {b} é {faz_som(Menor,maior)}")