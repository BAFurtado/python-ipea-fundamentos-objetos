import pandas as pd

# path = r'/home/b/curso/minha.csv'
# r -> raw-string literal. se a barra \ ou // windows /, o r faz com que todos os caminhos sejam reconhecidos
import os
os.getcwd()  # get current working directory
os.listdir() 
# for i in range(5):
#     files = os.lisdir()
# censo exemplo
# pnadc

if __name__ == '__main__':
    p = 'data/CO2 efficiency (1990-2016).xlsx'
    d = pd.read_excel(p)
    print(d.columns)
