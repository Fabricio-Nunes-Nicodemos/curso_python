"""
Higher Order Function
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}'


def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, 'Bom dia', 'Fabricio')
)

print(
    executa(saudacao, 'Boa noite', 'Maria')
)