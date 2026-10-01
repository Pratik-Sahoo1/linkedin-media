import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

F = "DejaVu Sans"
W, H, DPI = 1080, 1350, 100
OUT = "/home/claude/linkedin-media/posts"


def canvas(bg):
    fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI)
    fig.patch.set_facecolor(bg)
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, fc, ec="none", r=14):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec, lw=2))


# ===== Sat 3 Oct: 8 weeks red (dark, dramatic) =====
BG, INK, INK2, MUTED, TILE = "#1a1a19", "#ffffff", "#c3c2b7", "#8f8e86", "#262624"
RED = "#e66767"
fig, ax = canvas(BG)
ax.text(80, 105, "8 WEEKS IN THE RED.", color=INK, fontsize=44, fontweight="bold", family=F, va="center")
ax.text(80, 172, "5 NUMBERS EXPLAIN WHY.", color=INK, fontsize=44, fontweight="bold", family=F, va="center")
ax.text(80, 238, "Nifty's longest weekly losing streak in 25 years", color=INK2, fontsize=20, family=F, va="center")
# streak strip
for i in range(8):
    box(ax, 80 + i * 117, 285, 105, 46, RED, r=8)
    ax.text(80 + i * 117 + 52, 308, f"W{i+1}", color=BG, fontsize=17, fontweight="bold", family=F, ha="center", va="center")
ax.text(80, 365, "Nifty -8.7% and Sensex -8.4% over the eight weeks to 1 Oct", color=INK2, fontsize=17, family=F, va="center")
tiles = [
    ("5.34%", "US 10-year yield", "highest since 2002"),
    ("$27.8B", "Foreign (FPI) selling", "year to date"),
    ("$100+", "Brent crude", "on US-Iran tensions"),
    ("₹96.1", "Rupee per US dollar", "two-month low"),
    ("₹1.13L cr", "Raised by ~100 IPOs", "this year: extra supply"),
]
ty, th, gap = 410, 150, 16
for i, (big, label, sub) in enumerate(tiles):
    y = ty + i * (th + gap)
    box(ax, 80, y, W - 160, th, TILE)
    ax.text(115, y + th / 2, big, color=INK, fontsize=44, fontweight="bold", family=F, va="center")
    ax.text(530, y + th / 2 - 22, label, color=INK, fontsize=22, fontweight="bold", family=F, va="center")
    ax.text(530, y + th / 2 + 20, sub, color=INK2, fontsize=18, family=F, va="center")
ax.text(80, H - 55, "Data to 1 Oct 2026: HDFC Sky, 5paisa, Invezz", color=MUTED, fontsize=15, family=F, va="center")
ax.text(W - 80, H - 55, "Pratik P Sahoo", color=INK2, fontsize=17, fontweight="bold", family=F, va="center", ha="right")
fig.savefig(f"{OUT}/2026-10-03/eight-weeks-red.png", dpi=DPI, facecolor=BG); plt.close(fig)

# ===== Tue 6 Oct: RBI cut/hold/hike (light) =====
BG, INK, INK2, MUTED, RULE = "#fcfcfb", "#0b0b0b", "#52514e", "#8a8984", "#e4e3df"
BLUE, ORANGE = "#2a78d6", "#eb6834"
fig, ax = canvas(BG)
ax.text(80, 105, "RBI'S HARDEST CALL", color=INK, fontsize=48, fontweight="bold", family=F, va="center")
ax.text(80, 172, "IN YEARS.", color=INK, fontsize=48, fontweight="bold", family=F, va="center")
ax.text(80, 238, "Policy decision: 7 Oct 2026 · Repo rate today: 5.25%", color=INK2, fontsize=20, family=F, va="center")
ax.text(80, 310, "RETAIL INFLATION (CPI), 2026", color=INK2, fontsize=17, fontweight="bold", family=F, va="center")
months = [("May", 3.93), ("Jun", 4.38), ("Jul", 4.45), ("Aug", 4.82)]
base_y, top_y = 760, 380
scale = (base_y - top_y) / 5.5
bw, step, x0 = 150, 230, 130
tgt_y = base_y - 4.0 * scale
for i, (m, v) in enumerate(months):
    x = x0 + i * step
    h = v * scale
    ax.add_patch(FancyBboxPatch((x, base_y - h), bw, h, boxstyle="round,pad=0,rounding_size=4", fc=ORANGE if v > 4 else BLUE, ec="none"))
    ax.text(x + bw / 2, base_y - h - 26, f"{v:.2f}%", color=INK, fontsize=22, fontweight="bold", family=F, ha="center", va="center")
    ax.text(x + bw / 2, base_y + 30, m, color=INK2, fontsize=19, family=F, ha="center", va="center")
ax.plot([100, W - 100], [base_y, base_y], color=RULE, lw=2)
ax.plot([100, W - 100], [tgt_y, tgt_y], color=INK2, lw=2, ls=(0, (6, 5)))
ax.plot([W - 330, W - 280], [310, 310], color=INK2, lw=2, ls=(0, (6, 5)))
ax.text(W - 100, 310, "RBI target 4%", color=INK2, fontsize=17, family=F, ha="right", va="center")
ry = 850
ax.plot([80, W - 80], [ry, ry], color=RULE, lw=2)
opts = [("CUT", "Helps growth and stocks, but risks the rupee"),
        ("HOLD", "Buys time; keeps the 'neutral' stance"),
        ("HIKE", "Defends the rupee and inflation; hurts growth")]
for i, (k, d) in enumerate(opts):
    y = ry + 70 + i * 92
    box(ax, 80, y - 32, 150, 64, "#f0efeb", r=10)
    ax.text(155, y, k, color=INK, fontsize=24, fontweight="bold", family=F, ha="center", va="center")
    ax.text(260, y, d, color=INK2, fontsize=20, family=F, va="center")
ax.text(80, H - 55, "CPI: MoSPI via Business Standard, Republic · RBI", color=MUTED, fontsize=15, family=F, va="center")
ax.text(W - 80, H - 55, "Pratik P Sahoo", color=INK2, fontsize=17, fontweight="bold", family=F, va="center", ha="right")
fig.savefig(f"{OUT}/2026-10-06/rbi-hardest-call.png", dpi=DPI, facecolor=BG); plt.close(fig)

# ===== Sat 10 Oct: trade deal timeline (light) =====
fig, ax = canvas(BG)
ax.text(80, 105, "'DONE AND DUSTED'", color=INK, fontsize=48, fontweight="bold", family=F, va="center")
ax.text(80, 172, "TO 'INTERIM'.", color=INK, fontsize=48, fontweight="bold", family=F, va="center")
ax.text(80, 238, "One week in the India-US trade deal, and what it means", color=INK2, fontsize=20, family=F, va="center")
events = [("25 Sep", "Goyal: deal almost 'done and dusted'"),
          ("26 Sep", "US official: '90 per cent plus there'"),
          ("30 Sep", "Modi and Trump speak by phone"),
          ("1 Oct", "Goyal meets USTR Greer: 'interim agreement'")]
lx, y0, dy = 110, 340, 120
ax.plot([lx, lx], [y0, y0 + dy * (len(events) - 1)], color=RULE, lw=3)
for i, (d, e) in enumerate(events):
    y = y0 + i * dy
    ax.add_patch(plt.Circle((lx, y), 13, color=ORANGE if i == len(events) - 1 else BLUE, zorder=3))
    ax.text(lx + 40, y - 18, d, color=INK, fontsize=21, fontweight="bold", family=F, va="center")
    ax.text(lx + 40, y + 18, e, color=INK2, fontsize=19, family=F, va="center")
ry = 800
ax.plot([80, W - 80], [ry, ry], color=RULE, lw=2)
ax.text(80, ry + 50, "WHY MARKETS CARE", color=INK2, fontsize=17, fontweight="bold", family=F, va="center")
pts = ["Tariff certainty for Indian exporters to the US",
       "A clear deal could ease foreign (FPI) selling",
       "Sticking points: tariff edge vs rivals, Russian oil",
       "Next watch: Rubio's India visit in October"]
for i, s in enumerate(pts):
    ax.text(80, ry + 105 + i * 50, "→  " + s, color=INK, fontsize=20, family=F, va="center")
ax.text(80, H - 55, "Sources: Business Today, India Weekly", color=MUTED, fontsize=15, family=F, va="center")
ax.text(W - 80, H - 55, "Pratik P Sahoo", color=INK2, fontsize=17, fontweight="bold", family=F, va="center", ha="right")
fig.savefig(f"{OUT}/2026-10-10/india-us-trade-deal.png", dpi=DPI, facecolor=BG); plt.close(fig)
print("ok")
