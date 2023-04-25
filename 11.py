#1º função
def fatorial(n):
    calc_fat = 1
    for i in range(n,1,-1):
        calc_fat = calc_fat * i
    return calc_fat

#2º função 
def resultado(fat_n, fat_p, fat_np):
    res = 0
    res = fat_n / (fat_p * fat_np)
    return res

#3º função
n = int(input('Digite o valor de N: '))
p = int(input('Digite o valor de P: '))

fat_n = fatorial(n)
fat_p = fatorial(p)
fat_np = fatorial(n-p)
fat_res = resultado(fat_n, fat_p, fat_np)

print('A combinação de {} elementos, {} a {}, é igual à {}'.format(n,p,p,fat_res))