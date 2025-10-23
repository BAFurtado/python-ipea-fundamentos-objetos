
## Endereços  

- **Curso**: [https://bafurtado.github.io/python-ipea-fundamentos-objetos](https://bafurtado.github.io/python-ipea-fundamentos-objetos/)
- **Repositório git com os arquivos**: [https://github.com/baFurtado/python-ipea-fundamentos-objetos/](https://github.com/baFurtado/python-ipea-fundamentos-objetos/)

## A. Conditions
1. Em **python** use: `True` and `False`. Com a primeira maiúscula. 
2. São equivalentes a 1 e 0. 
3. É um tipo: `type(True)` `bool`
4. Também existem os operadores lógicos `and` `or` and  `not`
```python
>>> 2 + 2 == 4  # True
>>> 2 + 3 == 4  # False
>>> not True == False  # True
>>> (2 + 2 == 4) and (2 + 3 == 4)  # False
```

5. Conditions começam com `if` terminam em dois pontos `:` e necessariamente identação de 4 **espaços** na linha abaixo. Em seguida, podem ter `else` or `elif`. Veja os exemplos.

```python
valor = 10
if valor > 10:
    print('valor acima do esperado.')
else:
    print('valor dentro do esperado.')

container = [9, 65, 7, 0, 4]
if valor in container:
    print('valor encontrado')
elif valor - 1 in container:
    print('valor imediatamente menor encontrado')
else:
    print('não achei nada.')
```

6. Uso de `while` # be careful. Não se esqueça de alterar a condição para que o loop se encerre.
```python
valor = 10
while valor >= 0:
    print(valor)
    valor -= 1
```
7. `break` encerra o loop de `while`. Sai! Quando a condição para o `break` é chamada. 
```python
valor = 10
while True:
    if valor > 100:
        break
    print(valor)
    valor += 1
```

## B. Loops

1. Loops começam com  `for` + item `in` iterable. Termina em dois pontos e necessariamente tem identação de 4 **espaços** na linha abaixo.

```python
# Mineiro vai à feira
sacola = ['queijo', 'goiabada', 'pao de queijo', 'torresmo', 'linguiça', 'café']
for item in sacola:
    print(item)

# Calculando ímpares
for num in range(10):
    if num % 2 == 0:
        print(num)
    else:
        pass

# Vogais maiúsculas
for letter in 'python is cool':
    if letter in ['a', 'e', 'i', 'o', 'u']:
        # end='' evita escrever na linha seguinte.
        print(letter.upper(), end='')
    else:
        print(letter, end='')
```

## C. Funções
*""" Funções são pedacinhos de códigos que facilitam a chamada repetidamente, organizam o código e compõem uma tarefa específica. """*

1. Você já viu algumas funções que existem no `namespace` geral do python

```python
# Exemplo de três funções encadeadas: print, sum e range
print(sum([range(10)]))
# Também acessamos type e help
# Essas funcionam porque já estão presentes no ambiente geral
# Tamanho (len) também é uma função muito útil
print(len('python is cool'))
```

2. Funções começam sempre com a palavrinha `def`, terminam em dois pontos e necessariamente exigem 4 espaços na linha abaixo. Usualmente levam parâmetros e podem modificar o objeto, imprimir ou retornar valores.

```python
def soma(a, b):
    return a + b
```

3. A função em si, como acima, somente é armazenada no namespace. Para executá-la, é necessário chamá-la em algum outro momento do seu programa.

```python
a = 7
b =  6
print(soma(6, 7))
```

4. Funções, como tudo o resto, são objetos. Portanto, podem ser passadas como parãmetros.
```python
def lemma():
    print('python is cool')

type(lemma)

def repeat(func):
    func()
    func()

repeat(lemma)
```

5. Funções que não retornam nada, retornam `None`
6. Parâmetros não-nomeados devem respeitar a ordem. No exemplo, o primeiro parâmetro é `a`, o segundo é `b`.
7. É possível nomear parâmetros e entrá-los em outra ordem.
8. Se não nomear, assume base é o primeiro, altura o segundo.

```python
def area_triangulo(base=None, altura=None):
    return base * altura / 2

print(area_triangulo(altura=10, base=8))
```

8. Variáveis dentro de funções só estão acessíveis dentro da função.
9. **NEVER EVER** nomeie variáveis com mesmo nome dentro e fora da função. Ainda que elas sejam diferentes.

## D. Namespaces

Namespaces e if `__name__ == '__main__'` revisitado

Dois modos de usar um script Python:

A. Como módulo: Quando é importado por outro script (apenas disponibiliza funções/classes)

B. Como programa: Quando é executado diretamente (roda o código completo)

**Todo programa Python precisa de um "ponto de entrada"**, onde a execução começa.

- Sem `if __name__ == '__main__'`: Tudo roda sempre, causando problemas quando importado

 - Com `if __name__ == '__main__'`: Controlamos o que roda em cada situação

### O Python lê e executa o script linha a linha, de cima para baixo:

1. imports e definições de funções (prepara tudo)

2. Executa o código "solto", fora de funções

Problema: **Código solto roda SEMPRE, mesmo quando importado**

Funções vs Código Solto:

✅ Funções: São "receitas" que ficam na memória, só executam quando chamadas

❌ Código solto (print(), cálculos): Executa IMEDIATAMENTE quando o arquivo é lido

Script bem organizado:
```python

    # importações
    import math


    # funções
    def ler_raio():
        # lógica da leitura do raio (por exemplo, de um arquivo)
        return raio

    def area_circulo():
        # lógica do cálculo. usa math.pi
        pass


    def main():
        raio = ler_raio()
        area = area_circulo(raio)
        print(area)


    if __name__ == '__main__':
        main()  # Ponto de entrada controlado

```

- Controle preciso: Decide o que é "preparação" vs "execução"
- Reutilização: Permite usar o mesmo arquivo como módulo E programa
- Organização: Separa claramente a estrutura da execução principal

### Exemplos
1. calculos_import.py
2. calculos_main.py
3. calculos_teste.py


### Lista de arquivos de exemplos

1. list_media.py
2. lists_generator.py
2. is_even.py
2. conditional1.py
3. soma.py
4. Compare com function3.py
4. function0.py
5. function1.py
6. function2.py
7. function4.py
8. function5_comentada.py
9. function7.py
10. namespaces_example.py
11. my_first_loop.py
11. **debug** F10 breakpoint 
- dic_basics.py
## Exercícios

### A. Probability with Python. Rascunho de uma simulação numérica...

Quantos alunos são necessários para que uma turma tenha
probabilidade quase 1 de ter dois aniversariantes no mesmo dia?

Rodando simulações, chegamos próximos a probabilidades. 
Por examplo:
1. Considere o ano com 365 dias.
2. Sorteie dias para aniversários (aumentando o número de
alunos) (`random.randint()`)
3. Com os dias dos aniversários em uma lista, verifique se há
algum duplicado. (várias possibilidades). Se não conseguir, use
`set()`
4. Faça vaŕias vezes (100). Conte quantos houve pelo menos um
duplicado.

### B. Faça o desafio histogram Aula2

