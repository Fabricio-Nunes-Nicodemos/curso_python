# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

lista1 = []
cliente1 = adiciona_clientes('luiz', lista1)
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')
print(cliente1)

cliente2 = adiciona_clientes('Elena')
adiciona_clientes('Maria', cliente2)
print(cliente2)

