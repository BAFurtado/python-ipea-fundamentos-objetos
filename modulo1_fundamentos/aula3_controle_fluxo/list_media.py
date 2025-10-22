import lists_generator


def media_lista(minha_lista):
    return sum(minha_lista) / len(minha_lista)


if __name__ == '__main__':
    lst_qq = lists_generator.generate(10)
    print(lst_qq)
    resultado = media_lista(lst_qq)
    print(resultado)
