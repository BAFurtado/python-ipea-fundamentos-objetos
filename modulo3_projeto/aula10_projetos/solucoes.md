
# Soluções e dicas 

Este documento contém **pistas, lógica e snippets parciais** para os exercícios.
Não são soluções completas.

---

## 1. Jogo do número secreto (0 a 100)

### Pontos críticos
- Converter `input()` para `int`
- Evitar loop infinito
- Contar tentativas
- Tratar erro de entrada

### Lógica
- Gerar número aleatório
- Loop `while`
- Comparações sucessivas
- `break` quando acertar

```python
import random

numero = random.randint(0, 100)
tentativas = 0
```

```python
while True:
    palpite = int(input("Digite um número: "))
    tentativas += 1
```

```python
if palpite < numero:
    print("Muito baixo")
elif palpite > numero:
    print("Muito alto")
else:
    print(f"Acertou em {tentativas} tentativas!")
    break
```

---

## 2. Fork de repositório no GitHub

### Pontos críticos
- Fork ≠ clone

    * Clone cria uma cópia local do repositório para você trabalhar, mas sem relação direta com o projeto original.
        
    * Fork cria uma cópia do repositório na sua conta do GitHub, permitindo propor alterações ao projeto original via pull request.

        * Fork é pegar uma cópia do caderno do colega.
        * Pull request é levantar a mão e dizer:
        * “Posso colar essa página no caderno original?”

    * Fork é feito no site do GitHub

- Commit antes de push
- Editar README corretamente

### Checklist lógico
```text
Fork → Clone → Editar → Add → Commit → Push
```

```bash
git add README.md
git commit -m "Inclui email institucional"
git push
```

---

## 3. Elasticidade-preço da demanda

### Pontos críticos
- Divisão por zero
- Listas com tamanhos diferentes
- Classificação correta

### Lógica
- Função com duas listas
- Variações percentuais
- Elasticidade média

```python
def elasticidade_preco(precos, quantidades):
    ...
    return elasticidade_media, classificacao
```

```python
if e > 1:
    tipo = "elástica"
elif e < 1:
    tipo = "inelástica"
else:
    tipo = "unitária"
```

---

## 4. Dicionário de municípios e PIB per capita

### Pontos críticos
- Uso correto de dicionários
- Funções `max` e `min`

```python
pib = {
    "Brasília": 85000,
    "São Paulo": 70000
}
```

```python
maior = max(pib, key=pib.get)
menor = min(pib, key=pib.get)
```

---

## 5. CSV de inflação (pandas)

### Pontos críticos
- Caminho do arquivo
- Rolling mean
- Filtro condicional

```python
import pandas as pd

df = pd.read_csv("inflacao.csv")
```

```python
df["media_6m"] = df["inflacao"].rolling(6).mean()
```

```python
df[df["inflacao"] > limiar]
```

---

## 6. GitHub Actions — execução automática

### Pontos críticos
- Cron em UTC
- Identação YAML
- Checkout obrigatório

```yaml
on:
  schedule:
    - cron: "0 21 * * 5"
```

```yaml
steps:
  - uses: actions/checkout@v3
  - uses: actions/setup-python@v4
    with:
      python-version: "3.10"
  - run: python main.py
```

---

## 7. Modelo simples de preços imobiliários

### Pontos críticos
- Modelo simples
- Separar treino e teste
- Explicar resultados

```python
from sklearn.linear_model import LinearRegression
```

```python
model = LinearRegression()
model.fit(X_train, y_train)
model.score(X_test, y_test)
```

---
# 7️⃣ Modelo simples de preços imobiliários 

---

##  Objetivo

Construir um modelo de regressão onde:

- a variável dependente é o **logaritmo do preço do imóvel**
- as variáveis explicativas são **características observáveis do imóvel**
- os coeficientes tenham **interpretação econômica clara**

Modelo conceitual:

![equation](https://latex.codecogs.com/svg.image?\log(P_i)=\beta_0+\beta_1X_{1i}+\beta_2X_{2i}+\dots+\varepsilon_i)

Onde:
- (P_i) é o preço do imóvel
- (X) são características como área, número de quartos, localização etc.

---

##  Intuição econômica

- Preços imobiliários costumam ser:
  - assimétricos
  - heterocedásticos
- Trabalhar com **log(preço)**:
  - aproxima variações percentuais
  - reduz influência de outliers
  - facilita interpretação dos coeficientes

Exemplo de interpretação:
> Um coeficiente de 0,05 indica aproximadamente **5% de variação no preço**
associada a uma variação unitária na covariável.

---

## Problemas prováveis

- Esquecer de aplicar log no preço
- Usar variáveis categóricas sem tratamento
- Interpretar coeficientes como causais
- Avaliar o modelo apenas pelo R²
- Criar um modelo excessivamente complexo

---

##  Lógica mínima esperada

1. Carregar os dados reais do CSV
2. Inspecionar e limpar os dados
3. Criar a variável `log_preco`
4. Selecionar covariáveis relevantes
5. Separar base de treino e teste
6. Estimar uma regressão linear
7. Avaliar o desempenho do modelo
8. Interpretar economicamente os resultados

---

## Snippets úteis (pistas)

### Log do preço
```python
import numpy as np

df["log_preco"] = np.log(df["preco"])
```

---

### Seleção de covariáveis (exemplo)
```python
X = df[["area", "quartos", "banheiros"]]
y = df["log_preco"]
```

---

### Separação treino / teste
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
```

---

### Regressão linear
```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

---

### Avaliação básica
```python
r2 = model.score(X_test, y_test)
```

---

## 📊 Visualização mínima recomendada

```python
import matplotlib.pyplot as plt

plt.scatter(y_test, model.predict(X_test), alpha=0.5)
plt.xlabel("log(preço observado)")
plt.ylabel("log(preço previsto)")
plt.plot(y_test, y_test)
plt.show()
```

Objetivo do gráfico:
- identificar viés
- avaliar dispersão
- discutir limitações do modelo

---


