import matplotlib.pyplot as plt
import numpy as np

fig1 = plt.figure()  # an empty figure with no axes

# Gere 100 valores de 0 a 2
x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear', color='black')
plt.plot(x, x**2, label='quadratic', color='pink')
plt.plot(x, x**3, label='cubic', color='brown')

#
plt.xlabel('x label')
plt.ylabel('y label')
#
plt.title("Simple Plot")
plt.legend(frameon=False)
plt.show()