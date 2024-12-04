
"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)


# from itertools import zip_longest
# lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
# print(lista_soma) 


# for item in range(len(lista_b)):
#     lista_soma.append(lista_a[item] + lista_b[item])
# print(lista_soma)


# for indice, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[indice] + lista_b[indice])
# print(lista_soma)