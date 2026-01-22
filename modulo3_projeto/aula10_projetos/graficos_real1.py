import pandas as pd
import matplotlib.pyplot as plt

import groups_cols

colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']


def plotting(data, name='name'):
    lbsl = [groups_cols.abm_dummies_show[l] for l in data.index.tolist()]
    fig, ax = plt.subplots(figsize=(8, 6))

    policies = [
        'POLICIES_buy',
        'POLICIES_rent',
        'POLICIES_wage',
        'POLICIES_no_policy'
    ]

    labels = [
        'Purchase',
        'Rent vouchers',
        'Monetary aid',
        'No-policy baseline'
    ]

    for i, (pol, label) in enumerate(zip(policies, labels)):
        ax.scatter(
            data.index,
            data[pol],
            color=colors[i],
            alpha=.6,
            marker='o',
            label=label
        )

    ax.vlines(
        x=range(len(lbsl)),
        ymin=0, ymax=1,
        colors='lightgrey', lw=.8, alpha=.5
    )

    ax.set_xticks(range(len(lbsl)))
    ax.set_xticklabels(lbsl, rotation='vertical', fontsize=9)

    ax.set_ylabel("Percentage of Metropolitan Regions' optimal cases per policy")
    ax.legend(
        edgecolor='white',
        loc='upper center',
        facecolor='white',
        framealpha=1
    )

    plt.tight_layout()
    plt.savefig(f'graph_real_sorted_{name}.png', dpi=300)
    plt.show()



if __name__ == '__main__':
    p = '../../data/IQR.csv'
    d = pd.read_csv(p, sep=';')
    d.drop('Unnamed: 0', inplace=True, axis=1)
    pivoted_d = pd.pivot(d, index='ACP', columns='pol', values='mean')

    pivoted_d.sort_values(by='POLICIES_no_policy', ascending=False, inplace=True)
    plotting(pivoted_d, name='POLICIES_no_policy')
