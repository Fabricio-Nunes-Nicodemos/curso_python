"""
Operação ternária (condicional de uma linha)
<valor> if <condical> else <outro valor>
"""

# condicao = 10 == 11
# variavel = 'Valor' if condicao else 'Outro Valor'
# print(variavel)

# digito = 10
# novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)

print('valor' if True else 'Outro valor' if True else 'Fim')
