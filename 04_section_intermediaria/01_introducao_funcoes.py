"""
Introdução às funções (def) em Python
Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Eles podem receber valores para parâmetros (argumentos) e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Fabricio')
saudacao('Pedro')
saudacao('Maria')
saudacao()