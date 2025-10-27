

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
# 1. Cria uma instância. Um objeto do tipo AnalisaDataset
analisador = AnalisaDataset("Vendas 2024")
# 2. Usa o método carregar_dados que está embutido no objeto analisador que é uma instância da classe AnalisaDataset
analisador.carregar_dados({"produtos": [100, 150, 200], "precos": [29.90, 49.90, 79.90]})
# 3. Usa outro método
media_precos = analisador.calcular_media("precos")
print(f"Média dos preços: R${media_precos:.2f}")
# 4. Média produtos
media_produtos = analisador.calcular_media("produtos")
print(f"Média dos produtos: {media_produtos}")
