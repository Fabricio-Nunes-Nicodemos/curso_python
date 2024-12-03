# Manipulando chaves e valores em dicionários

pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Fabrício Nicodemos'
pessoa['sobrenome'] = 'Miranda'

print(pessoa[chave])

pessoa[chave] = "Maria"

del pessoa['sobrenome']
print(pessoa)