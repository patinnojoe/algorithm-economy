import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from src.config import OUTPUT_DIR

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