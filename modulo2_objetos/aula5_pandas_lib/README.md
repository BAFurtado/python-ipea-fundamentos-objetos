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


