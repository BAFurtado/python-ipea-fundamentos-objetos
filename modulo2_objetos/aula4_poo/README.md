# Aula 4: Introdução a Classes em Python

### Por que Classes

- Embora bibliotecas como Pandas (próxima aula) abstraiam muita complexidade, entender classes é fundamental para:

    - Organizar código de análise de dados de forma estruturada

    - Criar processamentos personalizados 

    - **Chave**  
        Entender como bibliotecas como Pandas e ML funcionam internamente

### Conceitos Básicos de Classes

- método `__init__` é o construtor. Roda ao criar um objeto
- `self.` referencia o próprio objeto. Padrão em toda classe. Acessa métodos internos
- **instância**, instanciar: objeto, criar objeto do tipo Classe


```python
class AnalisaDataset:
    """Classe básica para análise de datasets"""
    
    def __init__(self, nome_dataset):
        # Método construtor - inicializa o objeto
        self.nome = nome_dataset
        self.dados = None
        self.metricas = {}
    
    def carregar_dados(self, dados):
        """Carrega dados para análise"""
        self.dados = dados
        print(f"Dados carregados para {self.nome}")
    
    def calcular_media(self, coluna):
        """Calcula média de uma coluna"""
        if self.dados is not None:
            return sum(self.dados[coluna]) / len(self.dados[coluna])
        return None

# Uso prático
analisador = AnalisaDataset("Vendas 2024")
analisador.carregar_dados({"produtos": [100, 150, 200], "precos": [29.90, 49.90, 79.90]})
media_precos = analisador.calcular_media("precos")
```

## Exemplos práticos


1. `my_zero_class.py`
2. my_first_class.py
3. class_template.py
4. inheritance: my_second_class.py
5. Use of classes. Simple examples. Objetos

## Persistência


