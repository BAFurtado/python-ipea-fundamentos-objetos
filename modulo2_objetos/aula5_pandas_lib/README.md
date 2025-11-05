# Aula 5--Pandas

### Biblioteca de entrada de bases de dados e DataFrames
- Necessita estar presente no ambiente... ver: - [Instalação do Python, VS Code e ferramentas essenciais]({{ site.baseurl }}/configuracao/)

Teste: 

```python
import pandas as pd
print(pd.__version__)
```

```python
# Ajuste rápido
# No terminal
pip install pandas
```

- **Pandas se utilizem de DataFrames que contém linhas e colunas nomeadas.** 

- **Ou pelo nome da coluna ou pelo index da linha!**

No intuito de treinar, antes de ler bases reais, podemos entrar com dados em formato de dicionário, com as chaves correspondendo aos nomes de colunas e valores em formato de listas. A título de exemplo...

```python

data = {
    'name': ['Joao', 'Jose', 'Maria', 'Antonia', 'Luiza'],
    'city': ['BH', 'Brasília', 'Rio', 'Macaé', 'Porto Seguro'],
    'id': [41, 28, 33, 34, 38],
    'py-score': [88.0, 79.0, 81.0, 80, 0]
}

data = pd.DataFrame(data)
```

1. Quando não há explicitação de `index`, as linhas são numerados de 0 até `len(dados)`. Ou seja, quando as linhas não são explicitamente nomeadas. 

### Examinando os dados *no console*

1. `data.head()`  # Cinco elementos é o default. Aceita qualquer n.  `data.head(20)`
2. `data.tail()`  # Últimos elementos.
3. Muito útil `data.columns`  # Nomes de colunas, pois head pode suprimir dados, quando há muitas colunas
4. Simplesmente `data` *no console*, lista primeiros e últimos dados e colunas.
5. `data['city']`  # Seleciona a coluna com o nome da coluna entre colchetes
    - Se quiser, pode utilizar `.iloc` para acessar o índice (número da coluna, ou da linha)
    - Caso não haja espaço no nome da coluna, pode-se usar diretamente ponto `data.city`
6. `data.loc[2, 'id']`  # Acessa a linha 2 e a coluna id

### Criando pandas DataFrames
1. Com dicionários, como exemplificado
2. Com nested lists, ou numpy.arrays, explicitando nomes de colunas.
    - Caso contrário, colunas, como indexes, quando não explicitados são numéricos, começando em 0. 
    - `import numpy as np`
    - `data = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))`
    - `data = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['x', 'y', 'z'])`


### Lendo DataFrames from data
<img src="../../images/pandas_read_.png">

### Mais exames...

7. `data.info()`  # Identifica tipo de objeto e non-nulls
8. `data.describe()`  # Média, min, max, quantiles... para numeric columns
9. `data[col].value_counts()`  # Calcula números de itens de uma *Series* == coluna


