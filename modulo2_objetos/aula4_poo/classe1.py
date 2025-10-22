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
print(type(analisador))
print(help(analisador))
analisador.carregar_dados({"produtos": [100, 150, 200], "precos": [29.90, 49.90, 79.90]})
media_precos = print(f'Média preços: ${analisador.calcular_media("precos"):.2f}')
media_produtos = print(f'Média quantidade produtos: {analisador.calcular_media("produtos"):.2f}')
