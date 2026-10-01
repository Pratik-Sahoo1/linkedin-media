"""DuPont comparison: LinkedIn image (1080x1350) + short motion video."""
import os, subprocess, shutil
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

BG = "#1a1a19"
INK = "#ffffff"
INK2 = "#c3c2b7"
MUTED = "#7d7c75"
GRID = "#2e2e2c"
A_COL = "#3987e5"   # series slot 1 (dark)
B_COL = "#d95926"   # series slot 2 (dark)
FONT = "DejaVu Sans"

rows = [
    ("Net margin", 15.0, 3.0, "{:.0f}%"),
    ("Asset turnover", 0.8, 1.5, "{:.1f}x"),
    ("Equity multiplier", 1.5, 4.0, "{:.1f}x"),
]

W, H, DPI = 1080, 1350, 100


def ease(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def draw(progress=1.0, reveal=1.0, path="frame.png"):
    fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI)
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")

    # Header
    ax.text(80, 110, "SAME ROE.", color=INK, fontsize=50, fontweight="bold", family=FONT, va="center")
    ax.text(80, 180, "DIFFERENT RISK.", color=INK, fontsize=50, fontweight="bold", family=FONT, va="center")
    ax.text(80, 250, "The DuPont breakdown: ROE = margin × turnover × leverage",
            color=INK2, fontsize=19, family=FONT, va="center")

    # Legend (always present for 2 series)
    for i, (name, col) in enumerate([("Company A", A_COL), ("Company B", B_COL)]):
        x = 80 + i * 300
        ax.add_patch(FancyBboxPatch((x, 315), 26, 26, boxstyle="round,pad=0,rounding_size=5", fc=col, ec="none"))
        ax.text(x + 40, 328, name, color=INK, fontsize=20, family=FONT, va="center")

    # Rows: each lever on its own scale (different units), paired bars
    top, row_h, bar_h, gap = 400, 205, 52, 2
    x0, xmax = 80, 860
    for r, (label, a, b, fmt) in enumerate(rows):
        y = top + r * row_h
        ax.text(x0, y, label.upper(), color=INK2, fontsize=17, fontweight="bold", family=FONT, va="center")
        ax.plot([x0, x0], [y + 25, y + 25 + 2 * bar_h + gap], color=GRID, lw=2)
        scale = (xmax - x0) / max(a, b)
        for k, (v, col) in enumerate([(a, A_COL), (b, B_COL)]):
            by = y + 25 + k * (bar_h + gap)
            w = max(v * scale * progress, 1)
            ax.add_patch(FancyBboxPatch((x0, by), w, bar_h,
                                        boxstyle="round,pad=0,rounding_size=4", fc=col, ec="none"))
            ax.text(x0 + w + 14, by + bar_h / 2, fmt.format(v * progress if progress < 1 else v),
                    color=INK, fontsize=22, fontweight="bold", family=FONT, va="center", alpha=min(1, progress * 1.5))

    # Result
    ry = top + 3 * row_h + 20
    ax.plot([80, W - 80], [ry, ry], color=GRID, lw=2)
    if reveal > 0:
        al = reveal
        ax.text(80, ry + 70, "Both ROE = 18%", color=INK, fontsize=40, fontweight="bold", family=FONT, va="center", alpha=al)
        ax.text(80, ry + 135, "A earns it through profitability.", color=INK2, fontsize=21, family=FONT, va="center", alpha=al)
        ax.text(80, ry + 172, "B leans on 4x leverage, so it is far more fragile.",
                color=INK2, fontsize=21, family=FONT, va="center", alpha=al)

    ax.text(80, H - 55, "Illustrative numbers, not real companies", color=MUTED, fontsize=15, family=FONT, va="center")
    ax.text(W - 80, H - 55, "Pratik Sahoo", color=INK2, fontsize=17, fontweight="bold", family=FONT, va="center", ha="right")
    fig.savefig(path, dpi=DPI, facecolor=BG)
    plt.close(fig)


if __name__ == "__main__":
    out = os.path.dirname(os.path.abspath(__file__))
    draw(path=os.path.join(out, "dupont_post.png"))

    fdir = os.path.join(out, "frames"); shutil.rmtree(fdir, ignore_errors=True); os.makedirs(fdir)
    fps, total = 30, 9 * 30
    for i in range(total):
        t = i / fps
        prog = ease((t - 0.5) / 2.0)          # bars grow 0.5s -> 2.5s
        rev = ease((t - 3.0) / 0.8)            # result fades in at 3s
        draw(progress=prog, reveal=rev, path=os.path.join(fdir, f"f{i:04d}.png"))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps), "-i",
                    os.path.join(fdir, "f%04d.png"), "-c:v", "libx264", "-pix_fmt", "yuv420p",
                    "-crf", "18", "-movflags", "+faststart", os.path.join(out, "dupont_post.mp4")], check=True)
    shutil.rmtree(fdir)
    print("done")
