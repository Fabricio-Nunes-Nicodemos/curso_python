# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos;
# Retorne o total para uma variável e mostre o valor da variável.

def multiplicacao(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

print(multiplicacao(1, 2, 3, 4, 5))
print(1*2*3*4*5)

# Crie uma função que fala se um número é par ou ímpar. Retorne se o número é par ou ímpar.

def par_ou_impar(numero):

    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'O número {numero} é PAR'

    return f'O número {numero} é IMPAR'
    
print(par_ou_impar(12313223))