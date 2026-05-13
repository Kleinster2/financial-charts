"""
Bar chart: OpenAI 5-year cumulative compute spend vs hyperscaler annual capex.
One-off script for FT Apr 29 2026 ingestion.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "investing/attachments/openai-vs-hyperscaler-capex-2026.png"

labels = ["OpenAI\n(5yr cumulative\n2026-2030)", "AMZN\n2026 capex", "MSFT\n2026 capex", "GOOGL\n2026 capex", "META\n2026 capex"]
values = [600, 200, 190, 185, 135]
colors = ["#c1244c", "#7d7d7d", "#7d7d7d", "#7d7d7d", "#7d7d7d"]

# Revenue underneath for the capex/revenue annotation
revenue = [20, 638, 281, 365, 165]
ratios = [v / r for v, r in zip(values, revenue)]

fig, ax = plt.subplots(figsize=(11, 6.2), dpi=130)
fig.patch.set_facecolor("#fff8ed")
ax.set_facecolor("#fff8ed")

bars = ax.bar(labels, values, color=colors, edgecolor="black", linewidth=0.4, width=0.62)

for bar, v, r in zip(bars, values, ratios):
    ax.text(bar.get_x() + bar.get_width()/2, v + 12, f"${v}B", ha="center", va="bottom", fontsize=12, fontweight="bold")
    # Put capex/revenue annotation inside the bar near the bottom
    text_color = "white" if v > 150 else "#222"
    ax.text(bar.get_x() + bar.get_width()/2, 35, f"capex/rev\n{r:.1f}x", ha="center", va="bottom", fontsize=9.5, color=text_color, fontweight="bold")

ax.set_ylabel("$ billions", fontsize=11)
ax.set_title("OpenAI committed compute spend vs hyperscaler 2026 capex", fontsize=13, pad=14, loc="left")
ax.set_ylim(0, 720)
ax.tick_params(axis="x", labelsize=10)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#888")
ax.spines["bottom"].set_color("#888")
ax.tick_params(colors="#444")
ax.grid(axis="y", linestyle=":", alpha=0.4)

# Subtle annotation explaining the comparison (top right, off the bars)
ax.text(0.45, 0.97,
        "OpenAI commits $600B over five years (2026-2030).\n"
        "Big 4 hyperscalers commit $710B in 2026 alone.\n"
        "OpenAI's capex/revenue ratio is ~30x the hyperscalers'.",
        transform=ax.transAxes, fontsize=9.5, color="#333", va="top", ha="left",
        bbox=dict(facecolor="#fff", edgecolor="#ccc", boxstyle="round,pad=0.5"))

ax.text(0.99, -0.16, "Sources: FT Apr 29 2026 (OpenAI $600B); company Q1 2026 guides per Hyperscaler capex note. Revenue = TTM est.",
        transform=ax.transAxes, ha="right", fontsize=8, color="#666", style="italic")

plt.tight_layout()
plt.savefig(OUT, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"wrote {OUT}, size={OUT.stat().st_size} bytes")
