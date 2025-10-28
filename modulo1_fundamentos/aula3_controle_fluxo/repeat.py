def lemma():
    print('python is cool')
    print('python is not nasty')


def repete_funcao(f):
    f()
    f()

lemma()

repete_funcao(lemma)