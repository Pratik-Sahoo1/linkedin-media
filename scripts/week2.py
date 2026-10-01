import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

BG, INK, INK2, MUTED, RULE = "#fcfcfb", "#0b0b0b", "#52514e", "#8a8984", "#e4e3df"
BLUE, ORANGE = "#2a78d6", "#eb6834"
F = "DejaVu Sans"
W, H, DPI = 1080, 1350, 100


def canvas():
    fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI)
    fig.patch.set_facecolor(BG)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")
    return fig, ax


def footer(ax, note):
    ax.text(80, H - 55, note, color=MUTED, fontsize=15, family=F, va="center")
    ax.text(W - 80, H - 55, "Pratik P Sahoo", color=INK2, fontsize=17, fontweight="bold", family=F, va="center", ha="right")


# ---- Yield curve (Tue 6 Oct) ----
fig, ax = canvas()
ax.text(80, 110, "A SIGNAL,", color=INK, fontsize=50, fontweight="bold", family=F, va="center")
ax.text(80, 180, "NOT A SCHEDULE.", color=INK, fontsize=50, fontweight="bold", family=F, va="center")
ax.text(80, 250, "What an inverted yield curve does (and doesn't) tell you", color=INK2, fontsize=19, family=F, va="center")
for i, (name, col) in enumerate([("Normal curve", BLUE), ("Inverted curve", ORANGE)]):
    x = 80 + i * 330
    ax.add_patch(FancyBboxPatch((x, 315), 26, 26, boxstyle="round,pad=0,rounding_size=5", fc=col, ec="none"))
    ax.text(x + 40, 328, name, color=INK, fontsize=20, family=F, va="center")
# plot area
px0, px1, py0, py1 = 140, 1000, 420, 880
ax.plot([px0, px0], [py0, py1], color=RULE, lw=2); ax.plot([px0, px1], [py1, py1], color=RULE, lw=2)
mats = ["3M", "1Y", "2Y", "5Y", "10Y", "30Y"]
xs = np.linspace(px0 + 40, px1 - 20, len(mats))
for x, m in zip(xs, mats):
    ax.text(x, py1 + 32, m, color=INK2, fontsize=17, family=F, ha="center", va="center")
ax.text(px0 - 20, (py0 + py1) / 2, "Yield", color=INK2, fontsize=17, family=F, ha="center", va="center", rotation=90)
ax.text((px0 + px1) / 2, py1 + 72, "Time to maturity", color=INK2, fontsize=17, family=F, ha="center", va="center")
t = np.linspace(0, 1, 200)
xx = px0 + 40 + t * (px1 - 20 - px0 - 40)
normal = py1 - 90 - 280 * (1 - np.exp(-3.2 * t)) / (1 - np.exp(-3.2))
inverted = py0 + 70 + 230 * (1 - np.exp(-3.2 * t)) / (1 - np.exp(-3.2))
ax.plot(xx, normal, color=BLUE, lw=5, solid_capstyle="round")
ax.plot(xx, inverted, color=ORANGE, lw=5, solid_capstyle="round")
ax.text(px1 - 10, normal[-1] - 30, "Long rates > short rates", color=INK, fontsize=16, family=F, ha="right", va="center")
ax.text(px1 - 10, inverted[-1] + 32, "Short rates > long rates", color=INK, fontsize=16, family=F, ha="right", va="center")
ry = 1000
ax.plot([80, W - 80], [ry, ry], color=RULE, lw=2)
lines = [("Usually comes before US recessions", INK),
         ("But the lead time ranges from months to over a year", INK2),
         ("2022-24: inverted ~2 years, no clear recession followed", INK2)]
for i, (s, c) in enumerate(lines):
    ax.text(80, ry + 60 + i * 52, ("+ " if i == 0 else "- ") + s, color=c, fontsize=22 if i == 0 else 20,
            fontweight="bold" if i == 0 else "normal", family=F, va="center")
footer(ax, "Illustrative curve shapes, not live data")
fig.savefig("/home/claude/linkedin-media/posts/2026-10-06/yield-curve.png", dpi=DPI, facecolor=BG)
plt.close(fig)

# ---- WeWork (Sat 10 Oct) ----
fig, ax = canvas()
ax.text(80, 110, "$47 BILLION", color=INK, fontsize=50, fontweight="bold", family=F, va="center")
ax.text(80, 180, "TO BANKRUPTCY.", color=INK, fontsize=50, fontweight="bold", family=F, va="center")
ax.text(80, 250, "WeWork and the danger of a duration mismatch", color=INK2, fontsize=19, family=F, va="center")
# timeline
ty = 360
ax.plot([110, W - 110], [ty, ty], color=RULE, lw=3)
events = [(110, "Jan 2019", "Valued at ~$47B"), (540, "Sep 2019", "IPO pulled"), (W - 110, "Nov 2023", "Files for bankruptcy")]
for x, d, e in events:
    ax.add_patch(plt.Circle((x, ty), 13, color=ORANGE if x != 110 else BLUE, zorder=3))
    ha = "left" if x == 110 else ("right" if x == W - 110 else "center")
    ax.text(x, ty + 48, d, color=INK, fontsize=19, fontweight="bold", family=F, ha=ha, va="center")
    ax.text(x, ty + 82, e, color=INK2, fontsize=17, family=F, ha=ha, va="center")
# mismatch bars
by = 560
ax.text(80, by, "THE MISMATCH", color=INK2, fontsize=17, fontweight="bold", family=F, va="center")
x0, full = 80, W - 160
ax.text(80, by + 55, "What it owed: long-term leases (many years)", color=INK, fontsize=19, family=F, va="center")
ax.add_patch(FancyBboxPatch((x0, by + 80), full, 56, boxstyle="round,pad=0,rounding_size=4", fc=BLUE, ec="none"))
ax.text(80, by + 185, "What it earned: short-term memberships", color=INK, fontsize=19, family=F, va="center")
ax.add_patch(FancyBboxPatch((x0, by + 210), full * 0.12, 56, boxstyle="round,pad=0,rounding_size=4", fc=ORANGE, ec="none"))
ax.text(x0 + full * 0.12 + 16, by + 238, "often month-to-month", color=INK2, fontsize=17, family=F, va="center")
ax.text(80, by + 320, "When demand drops, rent stays fixed. Revenue doesn't.", color=INK, fontsize=20, fontweight="bold", family=F, va="center")
ry = 1000
ax.plot([80, W - 80], [ry, ry], color=RULE, lw=2)
ax.text(80, ry + 55, "3 checks before you trust a growth story", color=INK, fontsize=22, fontweight="bold", family=F, va="center")
for i, s in enumerate(["1. Fixed obligations vs flexible revenue",
                       "2. Unit economics, not just totals",
                       "3. Growth funded by operations or new capital?"]):
    ax.text(80, ry + 105 + i * 44, s, color=INK2, fontsize=19, family=F, va="center")
footer(ax, "Bar lengths are illustrative")
fig.savefig("/home/claude/linkedin-media/posts/2026-10-10/wework-mismatch.png", dpi=DPI, facecolor=BG)
plt.close(fig)
print("ok")
