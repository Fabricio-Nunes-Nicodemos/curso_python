import json

caminho_arquivo = 'C:\\curso_python\\04_section_intermediaria\\arquivos\\'
caminho_arquivo += 'aula117.json'

# pessoa = {
    
#     'nome': 'Luiz Otávio 2',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],

#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,

# }

# with open(caminho_arquivo, 'w', encoding='utf-8') as arquivos:
#     json.dump(
#         pessoa, 
#         arquivos,
#         ensure_ascii=False,
#         indent=2,
#     )

with open (caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])
