<style>
#cabeca {
 position: top;
 width: 100%;
 height: 380px;
}
</style>
 
<header>
   <a href="https://bafurtado.github.io/python-ipea-fundamentos-objetos/">
 <img id = "cabeca" src ="{{ site.baseurl }}/images/banner.png">
 </a>
</header>

# Aula 2

### Endereços
- Curso: [https://bafurtado.github.io/python-ipea-fundamentos-objetos](https://bafurtado.github.io/python-ipea-fundamentos-objetos/)
- Repositório git com os arquivos: [https://github.com/baFurtado/python-ipea-fundamentos-objetos/](https://github.com/baFurtado/python-ipea-fundamentos-objetos/)

**Aula 1--recapitulando**
- Instalação?
- Console
- Script `python meu_script.py`
- Operadores, `type`
- Noções de objetos em **Python**


## Cont. Aula 1

4. `help()`

## Strings

1. Strings, como listas (que veremos) são uma sequência
2. Com isso, podem ser acessadas por meio de indexes
    - Lembre-se: em **python** indexing começa em 0.
    Logo: 
    ```python
    frase = 'python is cool'
    frase[1]  # ?
    ```
### Acessando itens (em strings e listas)

1. Use index, mas começe pelo **0**   `# como maioria das "linguagens" de programação`
2. *MUTABLE*: Quando você "assign" um valor novo, ele substitui o anterior

```python
>>> supermercado = ['banana', 'ovos', 'alface', 'leite']
>>> supermercado[2] = 'rúcula'
>>> supermercado

# What happens for supermercado[-1] ?
```

1. **Sobre iterables e indexes**
    - dois pontos (colon) são importantes dentro de colchetes para indexes
        - [início:fim(não incluído)]
        - **[4:7]** do então 4 até o antes do 7
            - note que o 7o. termo está incluído porque começou em 0
        - início omitido é 0
        - fim omitido é o último -1
        - logo **[:]** é a lista toda
 
 ```python
 # simples é uma lista para ficar mais visual a posição (listas -> aula2)
 simples = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
 
 Teste no console
 ```python
 simples[0]
 simples[-1]
 simples[4]
 simples[:4]
 simples[:]
 simples[-2:]
 simples[:-2]
 simples[-2:-2]
 # be careful
 simples[10]
 # note que só acessamos os itens. não modificamos as listas
 # métodos, todavia, alteram a lista inplace
 ```

### Strings--methods

```python
motivator = 'python is cool'
type(motivator)
motivator.capitalize()
help(str)
# endswith, isnum, isalpha, islower, isupper, join, 
# lower, split,s trip, title, zfill
motivator[6]
motivator.split(' ')

subject, verb, adjective = motivator.split(' ')
sintaxe_tuple = motivator.split(' ')

CNPJ_BB = 191
# be carefult
CNPJ_BB.zfill(14)
# what is the error?
# ...

str(CNPJ_BB).zfill(14)
```

## Reserved words

<img src="{{ site.baseurl }}/images/keywords.png">

## Built-in functions


<img src="{{ site.baseurl }}/images/builtin.png">


[Fonte imagens/Credit: 30 Days of Python](https://github.com/Asabeneh/30-Days-Of-Python/tree/master)

## Código pythonico

- **Cuidado com seu self futuro**
<img src="{{ site.baseurl }}/images/meme.jpeg">
- ### [PEP 8 -- Jeito pythonista de ser](pep8-python-style-guide.md)

### Boas práticas--DRY: don't repeat yourself
www.greenteapress.com/thinkpython/html/thinkpython005.html
1. **Encapsulation**

    *Wrapping a piece of code up in a function is called encapsulation. One of the benefits of encapsulation is that it attaches a name to the code, which serves as a kind of documentation. Another advantage is that if you re-use the code, it is more concise to call a function twice than to copy and paste the body!*
            
2. **Generalization**

    *Adding a **parameter** to a function is called generalization because it makes the function more general*

### For Fun

1. `import antigravity`
2. `import this`
3. [**Gamification I**](https://py.checkio.org)
4. [**Gamification II**](http://www.pythonchallenge.com/pc/def/0.html)
5. [Automatizando uma fazenda com **Python**](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/)

### [Links Úteis]({{ site.baseurl }}/referencias/)

### Exercícios

1. Quanto é '5' * 5?
2. `print(5 + 5)` é igual a `print('5' + '5')`? Why?
3. Quanto é :  `(25 ∗ (2 + 23)/54)2`
4. Quantas horas inteiras tem em 200 minutos? Use `//` floor division
5. Quantos minutos sobram? Use `%` remainder

# Aula 2

Goal: Listas, tuplas, dicionários, conjuntos e suas operações principais. Exercícios

## Listas--mutable--iterable 

 - sequência (strings também)

```python
notas_curso = [0, 0, 1, 0, 3, 0, 2, 0, 9, 8]  # ;)
supermercado = ['banana', 'ovos', 'alface', 'leite']
total_mess = ['aulas', 43, ['October', 16]]
empty_list = list()
empty_list2 = []
```

### Métodos

1. `append(item)`  # appends to the end of the list
2. `pop()`  # returns last item
3. `sort()`  # accepts parameter `reverse` 
4. outras?

5. Apply **python** general functions to lists

```python
len(simples)
sum(simples)
# outras?
```
### Gotcha!

```python

a = [1, 2, 3]
b = a
a.append(4)
# What is the value of b?
# is serve para testar se o objeto é o mesmo
a is b
# id() é uma função que identifica o número individual do objeto na memória
id(a)
id(b)
```

### Fun thing (relacionada)
```python
a, b = 1, 2
# quais valores de a e de b?
a, b = b, a
# e agora?

# revisite total_mess
# o que total_mess[2][1] retorna?
```

## Tuplas (tuples)--immutable

```python
luck_numbers = (43, 16, 88)
type(luck_numbers)
help(luck_numbers)
16 in luck_numbers
69 in luck_numbers
luck_numbers.count(16)
luck_numbers[1]
```
1. Indexes igual à listas. 
2. Porém, imutável -> não recebe assignment  # Wrong: `t[0] = 9`

### Cool example: tuple + str method
```python
# introducing string formatting on the fly and join :)
print(f'join is {'super'.upper()} cool string method')
# systematics. print + f + single or double quotes + variable between brackets: 
print(f"this f-string works and is {adjective}")  
# as long as adjective exists in the namespace

# very common example tupla para assignment
hora = 60  # padrão
minutos = 200  # para transformar em horas e minutos

horas, minutos = minutos // hora, minutos % hora
```

## Dicionários key: value--muitíssimo útil--fast-indexado--mapping
```python
# Cria-se com CHAVES
# Par chave, valor com dois pontos
# Assign como listas, com colchetes--chave = valor

armario1 = {}
armario1 = dict()  # também funciona. Acho mais explícito
key = 'gavetao'
value = 'lençóis especiais'

# É necessário ter criado o dicionário antes. 
# Mesma coisa com append para lista.
armario1[key] = value
armario1
armario2 = {key: value}
armario2
armario3 = {'gavetao': 'lençóis especiais'}
armario3

armario1 == armario2 == armario3
armario1 is armario2
```

### Métodos

1. `armario1.keys()`  # chaves
2. `armario1.values()`  # valores
3. `armario1.items()`  # lista de tuples de chaves e valores 

    ```python
    armario1['gaveta_alta`] = 'pijamas
    [(key1, value1), (key2, value2)]
    armario1['gaveta_alta`] = 'pijamas
    ```

## Fun thing: salto ao futuro (das aulas)
### 🤔 good idea?

```python


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
palavra_teste = 'abracadabra'
resposta = histogram(palavra_teste)

```

## Sets--Conjuntos--elementos únicos!

```python
conjunto = set()
outro_conjunto = {87, 91, 88}  # Chaves, mas não para chave-valor. 
""" unordered, unchangeable, no duplicate values"""
# Method
conjunto.add(88)  # Não é append, como lista, é ADD
print(len(conjunto))
conjunto.add(88)
print(len(conjunto))
conjunto.add(81)
```

### Methods
 - `in` `88 in conjunto`
 - `conjunto.update(outro_conjunto)`  # também pode update com uma lista
 - `uniao = conjunto.union(outro_conjunto)`  # retorna um set
 - `conjunto.intersection(outro_conjunto)`  # mantém só os elementos, presentes em ambos, retorna um set
 - `diferenca = conjunto.difference(outro_conjunto)`  # retorna a diferença

### Vida prática--eliminar duplicates

`lista_elementos_unicos = list(set(lista_com_duplicados))`




