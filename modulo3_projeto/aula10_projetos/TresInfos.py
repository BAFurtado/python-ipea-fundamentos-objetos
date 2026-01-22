import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0], alpha=.7)
axs[0, 0].hist(data[1], alpha=.5, color='red')
axs[0, 0].hist(data[1] * data[0], bins=100, color='green')
axs[0, 1].scatter(data[0], data[1], marker='.', c='orange')
axs[1, 0].scatter(data[0], data[1], marker='*')
axs[1, 1].hist2d(data[0], data[1])

plt.tight_layout()
plt.show()