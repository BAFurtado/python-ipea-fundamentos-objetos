
var1 = 10


def teste(parametroa, parametrob):
    """
    parametroa : int
    parametrob : int
    retorna None
    """

def print_sentences():
    print('A vida é bela')
    print('Adoro Python')


def soma():
    """ Esta função realiza a soma de dois parametros do usuario
     """
    # Solicite um número ao usuário
    x = int(input('Entre um número: '))
    y = int(input('Entre outro número: '))
    print(f'A soma é: {x + y}')


if __name__ == '__main__':
    soma()
    print_sentences()
    # Teste não faz nada...
    teste(var1, 20)
