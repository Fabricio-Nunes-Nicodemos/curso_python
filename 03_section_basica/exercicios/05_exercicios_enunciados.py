"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# ****************** Minha versão ******************

# numero_usuario = input('Digite um número inteiro: ')

# try:
#     numero_inteiro = int(numero_usuario)
    
#     if numero_inteiro % 2 == 0:
#         print('Seu número é par')
#     else:
#         print('Seu número é ímpar')

# except:
#     print('Não é um número inteiro')

# ****************** Versão professor ******************

entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_str = 'ímpar'

    if par_impar:
        par_impar_str = 'par'

    print(f'O número {entrada_int} é {par_impar_str}')
else:
    print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# data_usuario = input("Digite algum horário inteiro: ")

# try:
#     data_usuario_inteiro = int(data_usuario)

#     if (data_usuario_inteiro > 0):
        
#         if (data_usuario_inteiro >= 0 and data_usuario_inteiro <=11):
#             print('Bom dia!')
#         elif (data_usuario_inteiro >= 12 and data_usuario_inteiro <= 17):
#             print('Boa tarde!')
#         else:
#             print('Boa noite!')

#     else:
#         print('Digite um valor maior que 0')

# except:
#     print('Não é um número inteiro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_usuario = input('Qual o seu nome?: ')
tamanho_nome = len(nome_usuario)

if tamanho_nome > 6:
    print('Seu nome é muito grande')
elif tamanho_nome < 6 and tamanho_nome >= 5:
    print('Seu nome é normal')
elif tamanho_nome <= 4:
    print('Seu nome é curto')