

def hour_converter(minutes):
    """ Função para converter minutos em horas e minutos
    Exemplifica floor division and modulus
    """
    # 1. Transformar de "format" para f-string
    # 2. Explicar main
    # função de conversão
    # duas barras // retorna a parte inteira da divisão
    h = minutes // 60
    # símbolo de percentual % -- retorna o resto (remainder)
    m = minutes % 60
    # assert h * 60 + m == minutes
    print(f'{h} hora(s) e {m} minuto(s)')


if __name__ == '__main__':
    # Ponto de entrada do programa. Parâmetros e sequência
    m = 343
    hour_converter(m)
