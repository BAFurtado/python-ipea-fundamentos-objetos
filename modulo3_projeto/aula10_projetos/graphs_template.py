"""
graphs_base.py
Basic matplotlib template (script style)

What this script shows:
- how to generate simple data
- how to create a figure and axes
- how to plot data
- how to customize the look of a graph
"""

import numpy as np
import matplotlib.pyplot as plt


def plotting(x, y):
        # --------------------------------------------------
    # 2. Create figure and axes
    # --------------------------------------------------
    # fig = the entire figure (canvas)
    # ax  = the plotting area (axes)

    fig, ax = plt.subplots(figsize=(8, 4))


    # --------------------------------------------------
    # 3. Main plots
    # --------------------------------------------------

    # Scatter plot (raw data)
    ax.scatter(
        x,
        y,
        color='tab:blue',
        alpha=0.6,
        label='Observed data'
    )

    # Line plot (trend / reference)
    ax.plot(
        x,
        np.sin(x),
        color='tab:red',
        linewidth=2,
        label='True function'
    )


    # --------------------------------------------------
    # 4. Axes labels and title
    # --------------------------------------------------
    ax.set_xlabel("x variable")
    ax.set_ylabel("y variable")
    ax.set_title("Example base plot (scatter + line)")


    # --------------------------------------------------
    # 5. Legend
    # --------------------------------------------------
    ax.legend(
        frameon=True,
        framealpha=1,
        edgecolor='white'
    )


    # --------------------------------------------------
    # 6. Visual cleanup (common publication style)
    # --------------------------------------------------

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Lighten remaining spines
    ax.spines['left'].set_alpha(0.7)
    ax.spines['bottom'].set_alpha(0.7)

    # Optional grid
    ax.grid(alpha=0.2)


    # --------------------------------------------------
    # 7. Layout, save, show
    # --------------------------------------------------
    plt.tight_layout()
    plt.savefig("example_base_plot.png", dpi=300)
    plt.show()


# --------------------------------------------------
# Main script
# --------------------------------------------------
if __name__ == "__main__":

    # --------------------------------------------------
    # 1. Generate a simple, interesting dataset
    # --------------------------------------------------
    np.random.seed(42)  # reproducibility

    x = np.linspace(0, 10, 50)

    # Introduce some noise
    y = np.sin(x) + 0.3 * np.random.randn(len(x))

    # Call function
    plotting(x, y)



