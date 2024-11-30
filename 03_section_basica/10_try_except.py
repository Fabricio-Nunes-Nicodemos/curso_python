"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobra o número que você digitar: ')

try:
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# print((numero_str.isdigit()))

# numero_float = float(numero_str)
# print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')


