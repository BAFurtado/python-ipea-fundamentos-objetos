## Panorama visualização + Projetos + Exercícios 

1. Biblioteca básica *python* Matplotlib. Default

`import matplotlib.pyplot as plt`

    - Exemplo simples
    - Crie 10,000 números aleatórios

    ``` python
    import numpy as np
    x = np.random.randn(10000)
    
    # Histogram simples
    plt.hist(x, bins=40, color='orange')
    plt.savefig('minha_figura.png')
    plt.show()
    
     ```

2. Plots básicos (e rápicos) para conferência dados

### Plot Linhas
- `plt.plot(x, y, marker='.', linestyle='-')`

### Plot dispersão
- `plt.scatter(x, y)`

### Boxplot
- `plt.boxplot(x)`

### Heatmap
- `plt.imshow(matriz)`

3. Mais de uma informação no mesmo gráfico: *`plt.figure()`*
- `Graphs2.py`

4. Várias figuras juntas. Várias informações em cada figura.
- Controle `fig, ax = plt.subplots()`
- `Tresinfos.py`

## Template para gráficos em *python*
- `graphs_template.py`


