string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3,'Eduarda']
tupla = 'python', 'é', 'legal'

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print('Maria', 'Helena', 1, 2, 3,'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

salas = [
    # 0         # 1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine'], # 1
    # 0        # 1      # 2
    ['Luiz', 'João', 'Eduarda', ], # 2
]

print(salas)
print(*salas, sep='\n')