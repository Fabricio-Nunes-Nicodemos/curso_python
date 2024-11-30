"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

CPF = '107.058.168-26'
cpf_formatado = ''
cpf_somado = 0
contador_regressivo_1 = 10
resultado_digito_1 = 0
tamanho_cpf = len(CPF)
cpf_gerado_pelo_calculo = ''

"""
Formato o CPF para que eu possa valida-lo
"""
if tamanho_cpf == 14:
    cpf_formatado = CPF.replace('.', '').replace('-','')[:9]
else:
    cpf_formatado = CPF[:9]


# Verifico o digito 1
for digito_1 in cpf_formatado:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# Verifico o digito 2
dez_digitos = cpf_formatado + str(digito_1)
contador_regressivo_2 = 11
resultado_digito_2 = 0
for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
dez_digitos += str(digito_2)

if tamanho_cpf == 14:
    contador = 0
    for numero in cpf_formatado:
    
        if contador == 3 or contador == 6:
            cpf_gerado_pelo_calculo += '.'
            cpf_gerado_pelo_calculo += numero
        
        else:
            cpf_gerado_pelo_calculo += numero
    
        contador += 1
    
    cpf_gerado_pelo_calculo += f'-{digito_1}{digito_2}'
else:
    cpf_gerado_pelo_calculo = f'{cpf_formatado}{digito_1}{digito_2}'

if CPF == cpf_gerado_pelo_calculo:
    print(f'{CPF} é valido')
else:
    print(f'CPF Inválido')
