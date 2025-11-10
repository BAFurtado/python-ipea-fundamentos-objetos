import numpy as np
import pandas as pd

from sectors_of_interest import list_muns, aps

columns_interest = [i for i in range(36, 136)] + [0, 23]


def extract_age_gender(male, female):
    """ Gather number of people by gender and age
    """
    result = list()
    for each in [male, female]:
        each['mun'] = each['Cod_setor'].astype(str).str[:7]
        each = each[each['mun'].isin(list_muns)]
        if len(each) == 0:
            return
        if 'Cod_se' in each.columns:
            # A file from SP has an extra column. I know. Go figure.
            each = each.drop('Cod_se', axis=1)
        each = each.iloc[:, columns_interest]
        new_columns = [str(int(x[2:]) - 34) if x.startswith('V0') and x != 'V022' else x for x in each.columns]
        new_columns = [str(int(x[1:]) - 34) if x.startswith('V') and x != 'V022' else x for x in new_columns]
        new_columns = ['0' if x == 'V022' else x for x in new_columns]
        each.columns = new_columns
        each = pd.merge(each, aps, on='Cod_setor', how='inner')
        # Some sectors with less than five residences, have omitted information, included as 'X'. Replace them
        each = each.replace('X', 0)
        each = each.astype(int)
        each = each.groupby('AREAP').agg(sum)
        each = each.drop('Cod_setor', axis=1)
        each = each.reset_index()
        result.append(each)
    male = result[0]
    female = result[1]
    male['gender'] = 2
    female['gender'] = 1
    return pd.concat([male, female])


def read_age_gender(keys):
    """ Auxiliary function to read age and gender from sectors tables
    """
    results = dict()
    output = pd.DataFrame()

    results['male'] = pd.read_csv(keys[0], sep=';')
    results['female'] = pd.read_csv(keys[1], sep=';')

    data = extract_age_gender(results['male'], results['female'])
    data = data.melt(id_vars=['AREAP', 'gender'], var_name='age')
    data = data.rename(columns={'value': 'num_people'})
    output = pd.concat([output, data])

    output.to_csv('temp_num_people_age_gender_AP.csv', sep=';', index=False)
    return output


def get_color(file):
    output = pd.DataFrame()
    data = pd.read_csv(file, sep=';')
    data = data[['Cod_setor', 'V002', 'V003', 'V004', 'V005', 'V006']]
    data = data.replace('X', 0)
    data = pd.merge(data, aps, on='Cod_setor', how='inner')
    data = data.astype(int)
    data = data.groupby('AREAP').agg(sum)
    data = data.drop('Cod_setor', axis=1)
    data = data.reset_index()
    names = ['branca', 'preta', 'amarela', 'parda', 'indigena']
    new = pd.DataFrame()
    new['AREAP'] = data['AREAP']
    for each in [1, 2, 3, 4, 5]:
        new[names[each - 1]] = data.apply(lambda x: x[each] / x[1:].sum(), axis=1)
    new = new.melt(id_vars=['AREAP'], var_name='cor')
    output = pd.concat([output, new])
    output.to_csv('temp_etnia_AP.csv', sep=';', index=False)
    return output


def get_wage_num_family(file):
    output = pd.DataFrame()

    data = pd.read_csv(file, sep=';', encoding='latin-1', decimal=',')
    # Variables of interest (mu, sigma for number of people per family and nominal wage)
    try:
        data = data[['Cod_setor', 'V003', 'V004', 'V009', 'V010']]
    except KeyError:
        data = data[['ï»¿Cod_setor', 'V003', 'V004', 'V009', 'V010']]
        data = data.rename(columns={'ï»¿Cod_setor': 'Cod_setor'})
    except KeyError:
        print('Problems with column name, using column index instead. Yes. Go figure IBGE')
        print(data.columns)
        data['Cod_setor'] = data.iloc[:, 0]
        data = data[['Cod_setor', 'V003', 'V004', 'V009', 'V010']]
    data = pd.merge(data, aps, on='Cod_setor', how='inner')
    # Average of averages and variances of sectors by weighted areas
    data = data.groupby('AREAP').agg('mean')
    data = data.drop('Cod_setor', axis=1)
    data = data.reset_index()
    output = pd.concat([output, data])
    output = output.rename(columns={'V003': 'avg_num_people', 'V004': 'var_num_people',
                                    'V009': 'avg_wage', 'V010': 'var_wage'})
    output.to_csv('temp_average_variance_family_wages.csv', sep=';', index=False)
    return output


if __name__ == '__main__':
    # Parece que só precisa atualizar num_people_age_gender

    p1 = r'Pessoa11_RO.csv'
    p2 = r'Pessoa12_RO.csv'
    k = [p1, p2]

    # mun_code = [1100122]

    output1 = read_age_gender(k)

    p3 = r'Pessoa03_RO.csv'
    output2 = get_color(p3)
    #
    p4 = r'Basico_RO.csv'
    output3 = get_wage_num_family(p4)

