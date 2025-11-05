# https://jakevdp.github.io/PythonDataScienceHandbook/index.html

# Needs html5lib `pip install html5lib`
import datetime
import pandas as pd
import requests
import matplotlib.pyplot as plt
# Tarefa: Get data for the top 20 for the past 10 weeks and plot?


headers = {'User-Agent': ''}


def get_past_weeks(ipt, n=7):
    # Transforme input em objeto datetime
    ipt = datetime.datetime.strptime(ipt, '%Y-%m-%d')
    # Make a list of past dates
    return [ipt - datetime.timedelta(days=7 * i) for i in range(n)]


def grouping(data, by, value):
    print(data.groupby(by).agg('mean')[value])


def get_table(path):
    rank = requests.get(path, headers=headers)
    rank = pd.read_html(rank.text)
    return rank[0]


def get_many_tables(start_day='2022-03-21'):
    out = pd.DataFrame()
    dates = get_past_weeks(start_day)
    for d in dates:
        # strftime: transforma objeto datetime em texto
        p2 = f"https://www.atptour.com/en/rankings/singles?rankRange=1-10&" \
             f"rankDate={datetime.datetime.strftime(d, '%Y-%m-%d')}"
        print(p2)
        t = get_table(p2)
        t = t[['Rank', 'Player', 'Points']]
        t['week'] = datetime.datetime.strftime(d, '%Y-%m-%d')
        out = out.append(t)
    return out


def plot_shinfrin(table):
    for each in table['Player'].unique():
        tab = table[table['Player'] == each]
        tab = tab.sort_values('week')
        plt.plot(tab['week'], tab['Points'], label=each)
        plt.text(tab.reset_index(drop=True).loc[len(tab) - 2]['week'],
                 tab.reset_index(drop=True).loc[len(tab) - 2]['Points'], each)
    # plt.legend(frameon=False)
    plt.show()


if __name__ == '__main__':
    p = 'https://www.atptour.com/en/rankings/singles?rankRange=1-5000&rankDate=2022-03-21'

    r = get_table(p)

    # r.loc[r.Age == r.Age.max()]['Player']
    # r.loc[r.Age == r.Age.min()]['Player']
    # len(r.loc[r.Age == 15])

    ts = get_many_tables()
    plot_shinfrin(ts)




