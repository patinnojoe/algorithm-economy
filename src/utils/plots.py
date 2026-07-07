import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from src.config import OUTPUT_DIR
from scipy.stats import kruskal, chi2_contingency



# Global theme
sns.set_theme(style="whitegrid")

FIG_WIDTH = 12
FIG_HEIGHT = 7

TITLE_SIZE = 20
LABEL_SIZE = 14
TICK_SIZE = 12

YOUTUBE_RED = "#FF0000"
DARK_RED = "#CC0000"
LIGHT_RED = "#FF4D4D"

PALETTE = sns.color_palette(
    [YOUTUBE_RED, LIGHT_RED, "#FF8080", "#FFB3B3"]
)
ALPHA = 0.05


# create figure canvas
def create_figure(*args, **kwargs):
    """
    Creates a matplotlib figure canvas.
    Works for single plots and multi-panel grids automatically.
    
    Usage:
      fig, ax = create_figure()                    # Single plot (Default)
      fig, axes = create_figure(nrows=1, ncols=3)  # Multi-plot matrix
    """
    if 'figsize' not in kwargs:
        # If building a multi-panel layout, scale the base figure size dynamically
        nrows = kwargs.get('nrows', 1)
        ncols = kwargs.get('ncols', 1)
        kwargs['figsize'] = (FIG_WIDTH * ncols, FIG_HEIGHT * nrows)
        
  
    fig, axes = plt.subplots(*args, **kwargs)
    
    return fig, axes

# plot figures
def style_plot(
    ax,
    title="",
    xlabel="",
    ylabel=""
):
    ax.set_title(
        title,
        fontsize=TITLE_SIZE,
        pad=20,
        weight="bold"
    )

    ax.set_xlabel(
        xlabel,
        fontsize=LABEL_SIZE
    )

    ax.set_ylabel(
        ylabel,
        fontsize=LABEL_SIZE
    )

    ax.tick_params(
        axis="both",
        labelsize=TICK_SIZE
    )

    sns.despine()
    
    
# save figures
def save_figure(
    fig,
    filename,
    dpi=300
):
    path = OUTPUT_DIR / filename

    
    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    fig.savefig(
        path,
        dpi=dpi,
        bbox_inches="tight",
        facecolor="white"
    )

    print(f"Saved: {path}")



# add source
def add_source(
    fig,
    text="Source: YouTube Data API v3"
):
    fig.text(
        0.01,
        0.01,
        text,
        fontsize=10,
        alpha=0.7
    )

# add bar labels
def add_bar_labels(ax, decimals=0): 
    fmt = f"%.{decimals}f"

    for container in ax.containers:
        ax.bar_label(
            container,
            fmt=fmt,
            fontsize=10
        )



# save figure
def save_table(df, filename, fontsize=10):
    fig, ax = plt.subplots(figsize=(12, len(df) * 0.35 + 1))
    ax.axis("off")

    table = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        loc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(fontsize)
    table.scale(1.2, 1.5)

    save_figure(fig, filename)
    plt.close(fig)
    


# eta interpretation
def interpret_eta_squared(eta):
    """
    Print an interpretation of Eta Squared.
    """

    if eta < 0.01:
        magnitude = "negligible"
    elif eta < 0.06:
        magnitude = "small"
    elif eta < 0.14:
        magnitude = "medium"
    else:
        magnitude = "large"

    print("=" * 60)
    print("Effect Size (Eta Squared)")
    print("=" * 60)
    print(f"Eta Squared : {eta:.4f}")
    print(f"Magnitude   : {magnitude.capitalize()} effect")
    print()
    print(
        f"Interpretation: Approximately {eta*100:.2f}% of the variation "
        f"in engagement rate is explained by video category."
    )
    print(
        f"The remaining {(1-eta)*100:.2f}% of the variation is attributable "
        "to other factors not captured by category."
    )
    
    
    # interepre kruskal
def interpret_test(name, statistic, pvalue):
    """
    Print a readable interpretation of a statistical test.
    """

    print("=" * 60)
    print(name)
    print("=" * 60)

    print(f"Test Statistic : {statistic:.3f}")
    print(f"P-value        : {pvalue:.6f}")

    if pvalue < ALPHA:
        print(f"Decision       : Reject H₀ (p < {ALPHA})")
        print("Interpretation : The observed differences are statistically significant.")
    else:
        print(f"Decision       : Fail to reject H₀ (p ≥ {ALPHA})")
        print("Interpretation : No statistically significant difference was detected.")

    print()