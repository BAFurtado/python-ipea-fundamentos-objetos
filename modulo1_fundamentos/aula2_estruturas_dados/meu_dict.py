def histogram(string): 
    """ Exemplo de dicionário como uma função para contagem: histogram. 
    Inclui parâmetro de input, retorna dicionário criado, faz loop e testa condicional. 
    Muita calma nessa hora!
    """
    # Cria o dicionário
    meu_dict = dict()
    # Começa o loop pelas letras da palavra
    for letter in string:
        # Testa se a letra já está no dicionário
        if letter not in meu_dict:
            # Inicia contagem
            meu_dict[letter] = 1
        # Se ela já estava, aumenta a contagem em 1
        else:
            meu_dict[letter] += 1
    # Depois do loop retorna o dicionário pronto
    return meu_dict

# Para chamar a função
palavra_teste = 'bernardo'
resposta = histogram(palavra_teste)
print(resposta)