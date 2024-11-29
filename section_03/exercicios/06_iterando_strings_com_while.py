"""
Iterando strings com while
"""

nome = "Fabrício Nicodemos"
tamanho_nome = len(nome)
acento = '*'
nova_string = ''
indice = 0

while indice < tamanho_nome:

    nova_string += acento + nome[indice]

    indice += 1

print(nova_string)