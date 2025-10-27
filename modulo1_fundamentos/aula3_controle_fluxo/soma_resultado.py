
def soma_inputs():

    minha_lista = []

    while len(minha_lista) != 2:
        try:
            x = float(input('Entre um número: '))
            minha_lista.append(x)
        except ValueError:
            print('Você não entrou um número... Por favorzinho, entre com um número inteiro')
    return sum(minha_lista)

if __name__ == '__main__':
    resultado = soma_inputs()
    print(f'A soma é: R${resultado:.2f}')   
