from pathlib import Path
import sys

import matplotlib.pyplot as plt
import pandas as pd

# Explicita diretório que contém este arquivo
BASE_DIR = Path(__file__).resolve().parent
# Deve apontar para a raiz do projeto. Nesse caso, 2 níveis acima (python 0, 1)
PROJECT_ROOT = BASE_DIR.parents[1]

sys.path.insert(0, str(PROJECT_ROOT))

from data import means_comparison


def dumbbell_plot(
    data,
    parameters,
    col_abm='z_simulated_optimal',
    col_ml='z_ml_optimal',
    name='dumbbell_plot'
):
    """
    Dumbbell plot comparing ABM vs ML optimal parameter means.
    """

    # Subset and sort by difference
    common = data.index.intersection(parameters)
    df = data.loc[common].copy()

    df['diff'] = df[col_ml] - df[col_abm]
    df = df.sort_values('diff')

    fig, ax = plt.subplots(figsize=(8, 4))

    # Y positions
    y = range(len(df))

    # Connecting lines (neutral)
    for i, (_, row) in enumerate(df.iterrows()):
        ax.plot(
            [row[col_abm], row[col_ml]],
            [i, i],
            color='lightgrey',
            lw=1,
            zorder=1
        )

    # Points
    ax.scatter(
        df[col_abm],
        y,
        color='tab:blue',
        label='ABM simulated optimal',
        zorder=2
    )

    ax.scatter(
        df[col_ml],
        y,
        color='tab:red',
        label='ML surrogate optimal',
        zorder=2
    )

    # Reference line
    # ax.axvline(0, color='black', lw=0.8, alpha=0.6)

    # Labels
    ax.set_yticks(y)
    ax.set_yticklabels(df.index, fontsize=10)
    ax.set_xlabel("Standardized mean value")
    ax.set_title("ABM vs ML optimal parameter comparison")

    # Legend
    ax.legend(
        frameon=True,
        facecolor='white',
        edgecolor='white',
        framealpha=1
    )

    plt.tight_layout()
    plt.savefig(f"{name}.png", dpi=300)
    plt.show()


if __name__ == '__main__':
    import os
    print(os.getcwd())
    o = pd.read_csv(PROJECT_ROOT / 'data/means_comparison_output_normTrue.csv', sep=';')
    o.rename(columns={'Unnamed: 0': 'param'}, inplace=True)
    o2 = pd.read_csv(PROJECT_ROOT / 'data/means_comparison_optimal_non_optimal_normTrue.csv', sep=';')
    o2.rename(columns={'Unnamed: 0': 'param'}, inplace=True)
    lst_parameters = means_comparison.different(o, o2)

    d = pd.read_csv(PROJECT_ROOT / 'data/parameters_norm_optimal.csv', sep=';')
    d.rename(columns={'Unnamed: 0': 'parameters'}, inplace=True)
    d = d.set_index('parameters')
    d = d.sort_values(by='difference')
    dumbbell_plot(
        data=d,
        parameters=lst_parameters,
        name='parameters_dumbbell'
    )