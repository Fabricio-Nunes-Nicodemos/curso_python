# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
def deve_ser_int_ou_float(numero):
    tipo_numero = type(numero)
    if not isinstance(numero, (float, int)):
        raise TypeError(f'"{numero}" deve ser int ou float. ', f'"{tipo_numero.__name__}" enviado')
    return True

def nao_aceito_zero(divisor):
    if divisor == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero, o que não é possível')
    return True

def divide(numero, divisor):
    
    deve_ser_int_ou_float(numero)
    deve_ser_int_ou_float(divisor)
    nao_aceito_zero(divisor)
    return numero / divisor


print(divide(8, '1'))