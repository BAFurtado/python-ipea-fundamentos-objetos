try:
    x = int(input('Entre um número: '))
except ValueError:
    print('Você não entrou um número... Por favorzinho, entre com um número inteiro')
    x = int(input('Entre um número: '))
y = int(input('Entre outro número: '))

# f-string
# python 3.6 para cá.
# texto corrido + variáveis
# print(f"Este é um texto de exemplo para a variável x {x}")
print(f'A soma é: R${x + y},00')


