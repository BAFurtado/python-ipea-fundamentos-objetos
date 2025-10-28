import lists_generator


def media_lista(minha_lista):
    return sum(minha_lista) / len(minha_lista)

def main():
    pass


if __name__ == '__main__':
    main()
    
    lst_qq = lists_generator.generate(1000000)
    print(lst_qq)
    resultado = media_lista(lst_qq)
    print(resultado)
