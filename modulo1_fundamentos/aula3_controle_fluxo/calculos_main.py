# calculos.py - Este é um módulo com funções de cálculo
import random


def calcular_media(numeros):
    """Calcula a média de uma lista de números"""
    return sum(numeros) / len(numeros)


def encontrar_maior_numero(numeros):
    """Encontra o maior número em uma lista"""
    return max(numeros)


def cria_lista():
    dados = list()
    for i in range(5):
        dados.append(random.randint(1, 100))
    return dados


def main():
    """Processa dados e retorna estatísticas"""
    dados = cria_lista()
    media = calcular_media(dados)
    maior = encontrar_maior_numero(dados)
    
    resultado = {
        'media': media,
        'maior_numero': maior,
        'quantidade': len(dados)
    }
    print(f'Análise lista aleatória: {resultado}')


if __name__ == '__main__':
    main()

