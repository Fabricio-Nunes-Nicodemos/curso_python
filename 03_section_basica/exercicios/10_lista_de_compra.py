import os

lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ').lower()

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        os.system('cls')
        indice_str = input('Escolha um índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite um número inteiro.')
        except IndexError:
            print('Índice não existe na lista.')
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada a listar\n')

        for i, valor in enumerate(lista):
            print(i, valor)

        print('\n')

    else:
        print('Por favor, escolha uma opção válida.')