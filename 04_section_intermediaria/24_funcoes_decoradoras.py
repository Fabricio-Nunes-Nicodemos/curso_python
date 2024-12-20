# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntex Sugar" (Açúcar sintático)


def create_function(func):
    def intern(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print(f'O seu resultado foi {result}')
        print('OK, agora você foi decorada')
        return result
    return intern


@create_function
def inverte_string(string):
    return string[::-1]


def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param should be an string')


invertida = inverte_string('123')
print(invertida)