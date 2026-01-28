import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# dados artificiais
df = pd.DataFrame({
    "grupo": ["A"] * 100 + ["B"] * 100,
    "valor": np.r_[np.random.rand(100),
                   np.random.randn(100) + 1]
})

sns.boxplot(data=df, x="grupo", y="valor")
plt.title("Comparação de distribuições por grupo")
plt.show()