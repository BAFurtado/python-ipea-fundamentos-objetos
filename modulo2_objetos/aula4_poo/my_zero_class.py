""" Exemplo de class
"""

# Começa com letra maiúscula
# Tem dois pontos e indentação. Normal.


class Abstract:

    # (quase) sempre tem uma def __init__ que gera o objeto padrão
    def __init__(self, texto):
        # Self refere-se a UMA instância do tipo da Classe Abstract
        self.texto = texto
        self.variavel = 0
        self.minha_lista = list()
        self.meu_dict = dict()

    def metodo1(self):
        # Os métodos são exatamente como funções
        # Funcionam internamente as classes e alteram variáveis e estruturas

        # Por exemplo o método pode alterar o valor da variável
        self.variavel += 10

    def metodo2(self, x):
        # Outro método pode adicionar elementos a uma lista
        self.minha_lista.append(x)

    def metodo3(self, key, value):
        self.meu_dict[key] = value

    def __repr__(self):
        return f'Eu sou o/a {self.texto}'


if __name__ == '__main__':
    # Criando instâncias abstratas
    minhas_instancias = list()
    for i in ['bob', 'john', 'mary', 'Carmela', 'Matilda']:
        minhas_instancias.append(Abstract(i))
    print(type(minhas_instancias[0]))
    print(minhas_instancias[0].texto)
    print(minhas_instancias[0])
    