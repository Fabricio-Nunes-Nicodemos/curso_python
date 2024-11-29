"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por dez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
texto = 'Fabricio'
numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)