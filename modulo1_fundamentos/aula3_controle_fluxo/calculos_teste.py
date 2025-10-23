# calculos.py - Este é um módulo com funções de cálculo

def calcular_media(numeros):
    """Calcula a média de uma lista de números"""
    return sum(numeros) / len(numeros)


def encontrar_maior_numero(numeros):
    """Encontra o maior número em uma lista"""
    return max(numeros)


def main(dados):
    """Processa dados e retorna estatísticas"""
    media = calcular_media(dados)
    maior = encontrar_maior_numero(dados)
    
    return {
        'media': media,
        'maior_numero': maior,
        'quantidade': len(dados)
    }


# CÓDIGO DE TESTE - Só roda quando executamos este arquivo diretamente
if __name__ == '__main__':
    # Dados de exemplo para teste
    dados_teste = [10, 20, 30, 40, 50]
    
    # Testando cada função
    print(f"Dados: {dados_teste}")
    print(f"Média: {calcular_media(dados_teste)}")
    print(f"Maior número: {encontrar_maior_numero(dados_teste)}")
    
    # Testando processamento completo
    resultado = main(dados_teste)
    print(f"Resultado completo: {resultado}")
