""" Files examples
"""
import os


def first():
    with open('experience.txt', 'w') as f:
        f.write('This is my first saved output\n')


def second():
    # Lembrando que se o W for informado incorretamente e o arquivo já existir,
    # O ARQUIVO SERÁ SOBREESCRITO. OVERWRITTEN!!!
    with open('experience.txt', 'a') as f:
        f.write('This is my second saved output\n')


# Let's try with some numbers:
def numbers():
    l = list()
    for i in range(10):
        l.append(i ** i)
    print(sum(l))
    with open('experience.txt', 'a') as f:
        for each in l:
            f.write(f'{each};')


# What have we done?
def reading():
    print(os.getcwd())
    with open('experience.txt', 'r') as f:
        lida = f.read()
    print(lida)
    return lida


def recover_list(li):
    li = li.split('\n')

    recovered = list()
    # porque o item 2? Use o debug para ver o conteúdo de li
    for each in li[2].split(';'):
        if len(each) > 0:
            recovered.append(int(each))

    print(recovered)
    return recovered


def sum_list(recovered):
    print('A soma da lista recuperada é {:,.0f}'.format(sum(recovered)))


if __name__ == '__main__':
    first()
    second()
    numbers()
    r = reading()
    ll = recover_list(r)
    sum_list(ll)
