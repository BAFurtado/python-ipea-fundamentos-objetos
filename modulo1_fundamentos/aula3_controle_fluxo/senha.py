""" Aprendendo sobre condicionais
    Preste atenção nos DOIS PONTOS depois da condição
    Note que 'else' é diferente de 'elif'
"""

import random


def adivinhacao(n=100):
    contador = 0
    sorteado = random.randint(0, n)
    
    while True:
        try:
            palpite = int(input(f'Digite um número inteiro entre 0 e {n}: '))
            contador += 1
            
            if palpite > sorteado:
                print('Seu número está alto... Tente um valor menor.')
            elif palpite < sorteado:
                print('Seu número está baixo... Tente um valor maior.')
            else:
                print('Parabéns! Você acertou!')
                print(f'Você precisou de {contador} tentativas')
                break
                
        except ValueError:
            print('Por favor, digite apenas números inteiros!')


if __name__ == '__main__':
    adivinhacao()
    