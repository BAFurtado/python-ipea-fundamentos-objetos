import pandas as pd


d = {
    'name': ['Joao', 'Jose', 'Maria', 'Antonia', 'Luiza', 
             'Enzo', 'Mauro', 'Lucas', 'Diana', 'Marcela'],
    'city': ['BH', 'Brasília', 'Rio', 'Macaé', 'Porto Seguro',
             'Valparaíso', 'Londrina', 'Jequié', 'Palmas', 'Santarém'],
    'id': [41, 28, 33, 34, 38, 70, 89, 100, 101, 105],
    'py-score': [88.0, 79.0, 81.0, 80, 0, 67, 54, 43, 23, 0]
    }
d = pd.DataFrame(d)

print(d)
print(d.head())
print(d.head(2))
print(d.tail())
print(d.columns)