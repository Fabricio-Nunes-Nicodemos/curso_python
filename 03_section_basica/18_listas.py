"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# lista.append(50)
# ultimo_valor = lista.pop()
# lista.append(60)
# lista.append('B')
# ultimo_valor = lista.pop()
# print(lista, 'Removido,', ultimo_valor)
# print(lista[2])

lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
lista.insert(0, 5)
print(lista)