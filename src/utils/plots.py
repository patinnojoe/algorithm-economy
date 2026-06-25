import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from src.config import OUTPUT_DIR

# Global theme
sns.set_theme(style="whitegrid")

FIG_WIDTH = 8
FIG_HEIGHT = 6

TITLE_SIZE = 18
LABEL_SIZE = 14
TICK_SIZE = 12


# create figure canvas
def create_figure():
    fig, ax = plt.subplots(
        figsize=(FIG_WIDTH, FIG_HEIGHT)
    )

    return fig, ax

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
    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    path = OUTPUT_DIR / filename

    fig.savefig(
        path,
        dpi=dpi,
        bbox_inches="tight"
    )

    print(f"Saved: {path}") 