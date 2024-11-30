"""
Lista de litas e seus índices
"""

salas = [
    # 0         # 1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine'], # 1
    # 0        # 1      # 2
    ['Luiz', 'João', 'Eduarda', ], # 2
]

# print(salas[0][1])

for sala in salas:
    for indice, aluno in enumerate(sala):
        print(indice, aluno)