import matplotlib.pyplot as plt
import numpy as np

# Distribuição normal
x = np.random.randn(10000)

# Histogram simples
plt.hist(x, bins=40, color='orange')
plt.savefig('minha_figura.png')
plt.show()

x.sort()
plt.plot(x, linestyle='-')
plt.show()

# Distribuição uniforme
y = np.random.rand(10000)

plt.scatter(x, y, marker='.', color='red', alpha=.1)
plt.show()

# Boxplot
plt.boxplot(x)
plt.show()

# Heatmap
matriz = np.random.rand(10, 10)

plt.imshow(matriz)
plt.colorbar()
plt.title("Heatmap simples")
plt.show()