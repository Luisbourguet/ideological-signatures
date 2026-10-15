# -*- coding: utf-8 -*-
"""Regenerate Fig. 2 (signature map) and Fig. 3 (operator graphs, two panels) for Firme 2.0.
ω values on a 0-10 scale from the project manifest (heatmap_firmas_ideologicas_omega.html)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'
CONF = ['C1 Survival', 'C2 Belonging', 'C3 Order', 'C4 Meaning', 'C5 Transformation']
SUB = ['S1 Biological', 'S2 Economic', 'S3 Political', 'S4 Cultural']
KEY = [['bodies kept\nalive', 'scarcity,\ndeprivation', 'enemy,\nsacrifice', 'saying\ndeath'],
       ['procreation,\nkin', 'work,\nmembership', 'border', 'language,\norigin'],
       ['natural\nhierarchy', 'possession', 'sovereignty,\nobedience', 'truth,\ncanon'],
       ['the human', 'worth,\ndesert', 'legitimacy', 'why this\nworld'],
       ['altering\nour nature', 'creative\ndestruction', 'reform or\nrupture', 'past that\nobliges']]
FAM = [
 ('Liberalism', [[1,5,2,1],[0,1,1,1],[0,10,3,1],[1,3,7,1],[0,4,4,1]], {(2,0):'∅',(1,2):'⇒',(1,3):'⇒'}, (2,1)),
 ('Socialism', [[2,9,1,0],[0,5,1,1],[0,9,4,1],[0,3,2,1],[1,3,4,0]], {(0,1):'⊕',(2,1):'⊕',(3,3):'⇒',(1,3):'⇒'}, (0,1)),
 ('Anarchism', [[1,3,0,1],[1,8,1,2],[0,6,0,1],[1,2,2,1],[0,3,5,1]], {(2,2):'∅'}, (1,1)),
 ('Conservatism', [[1,2,2,2],[5,1,1,3],[6,3,3,3],[2,1,2,5],[1,1,1,10]], {(4,1):'⇒',(2,0):'↓'}, (4,3)),
 ('Fascism', [[3,1,4,1],[10,0,7,3],[5,0,10,2],[1,0,2,0],[0,1,3,2]], {(1,0):'⊕',(2,2):'⊕',(0,1):'⇒',(3,3):'∅',(2,0):'↓'}, (1,0)),
 ('Nationalisms', [[1,2,3,1],[2,1,9,9],[1,1,4,2],[0,1,2,2],[0,1,1,3]], {(1,2):'⊕',(1,3):'⊕',(0,1):'⇒'}, (1,2)),
 ('Christian democracy', [[2,4,1,2],[8,2,2,3],[2,4,3,2],[2,2,3,8],[0,1,1,3]], {(1,0):'⊕',(3,3):'⊕',(0,1):'⇒'}, (1,0)),
 ('Ecologism', [[9,3,1,1],[1,1,1,2],[0,1,2,1],[2,1,1,2],[8,2,2,2]], {(0,0):'⊕',(4,0):'⊕✦',(0,1):'⇒'}, (0,0)),
 ('Feminisms', [[2,1,1,1],[7,2,1,2],[9,2,2,2],[4,1,1,2],[2,1,1,1]], {(2,0):'✦',(1,0):'✦'}, (2,0)),
 ('Accelerationism', [[1,4,1,0],[0,2,1,1],[0,3,2,1],[1,2,2,0],[2,10,4,0]], {(4,3):'∅',(3,3):'∅'}, (4,1)),
 ('Degrowth', [[2,4,1,0],[0,2,1,1],[0,3,2,1],[1,2,2,0],[3,10,3,0]], {(4,3):'∅',(3,3):'∅'}, (4,1)),
]
cmap = LinearSegmentedColormap.from_list('omega', ['#FFFFFF', '#E6E4F7', '#B9B3EC', '#7F77DD', '#4A41A8', '#26215C'])
INK = '#1F1F2E'; MUTED = '#6B6B80'
C_TR = '#1F6FB2'; C_FU = '#C8521E'; C_NA = '#5A7D2A'; C_SI = '#8A1C1C'; C_RE = '#A67C00'

def cell_xy(i, j):  # i row (0 top), j col
    return j, 4 - i

def draw_grid(ax, w, title, gravity):
    W = np.array(w, dtype=float); W = W / W.sum()
    vmax = 0.22
    for i in range(5):
        for j in range(4):
            x, y = cell_xy(i, j)
            ax.add_patch(FancyBboxPatch((x+0.05, y+0.05), 0.9, 0.9, boxstyle='round,pad=0,rounding_size=0.06',
                                        fc=cmap(float(min(W[i, j]/vmax, 1.0))), ec='#B8B8C8', lw=0.8))
            dark = W[i, j]/vmax > 0.55
            ax.text(x+0.1, y+0.86, f'({i+1},{j+1})', fontsize=7.5, color='#F2F2F8' if dark else MUTED, va='top', ha='left')
            ax.text(x+0.5, y+0.32, KEY[i][j], fontsize=6.3, color='#F2F2F8' if dark else INK, va='center', ha='center', linespacing=1.1)
    for (i, j) in (gravity if isinstance(gravity, list) else [gravity]):
        x, y = cell_xy(i, j)
        ax.add_patch(Rectangle((x+0.03, y+0.03), 0.94, 0.94, fc='none', ec=INK, lw=2.2))
    for j in range(4):
        ax.text(j+0.5, 5.12, SUB[j], ha='center', va='bottom', fontsize=8, color=MUTED)
    for i in range(5):
        ax.text(-0.08, 4-i+0.5, CONF[i], ha='right', va='center', fontsize=8, color=MUTED)
    ax.set_xlim(-1.7, 4.1); ax.set_ylim(-0.75, 5.45); ax.set_aspect('equal'); ax.axis('off')
    ax.set_title(title, fontsize=9, loc='left', color=INK, pad=10, fontweight='bold')

def num(ax, x, y, n, color):
    ax.add_patch(plt.Circle((x, y), 0.11, fc=color, ec='white', lw=0.8, zorder=6))
    ax.text(x, y, str(n), ha='center', va='center', fontsize=7, color='white', zorder=7, fontweight='bold')

def fusion(ax, a, b, n):
    (i1, j1), (i2, j2) = a, b
    x1, y1 = cell_xy(i1, j1); x2, y2 = cell_xy(i2, j2)
    for (x, y) in [(x1, y1), (x2, y2)]:
        ax.add_patch(Rectangle((x+0.03, y+0.03), 0.94, 0.94, fc='none', ec=C_FU, lw=2.2, ls=(0, (3, 1.5)), zorder=5))
    ax.plot([x1+0.5, x2+0.5], [y1+0.5, y2+0.5], color=C_FU, lw=5, alpha=0.28, solid_capstyle='round', zorder=4)
    mx, my = (x1+x2)/2+0.5, (y1+y2)/2+0.5
    ax.text(mx, my, '⊕', ha='center', va='center', fontsize=13, color=C_FU, zorder=6,
            bbox=dict(boxstyle='circle,pad=0.15', fc='white', ec=C_FU, lw=1))
    num(ax, x1+0.85, y1+0.85, n, C_FU)

def translation(ax, a, b, n):
    (i1, j1), (i2, j2) = a, b
    x1, y1 = cell_xy(i1, j1); x2, y2 = cell_xy(i2, j2)
    p = FancyArrowPatch((x1+0.5, y1+0.08), (x2+0.5, y2+0.92), connectionstyle='arc3,rad=-0.25',
                        arrowstyle='-|>', mutation_scale=14, color=C_TR, lw=1.6, zorder=6)
    ax.add_patch(p)
    mx, my = (x1+x2)/2+0.5-0.42, (y1+y2)/2+0.5+0.1
    ax.text(mx, my, '⇒', ha='center', va='center', fontsize=12, color=C_TR, zorder=7,
            bbox=dict(boxstyle='circle,pad=0.12', fc='white', ec=C_TR, lw=1))
    num(ax, x1+0.85, y1+0.85, n, C_TR)

def silencing(ax, a, n):
    i, j = a; x, y = cell_xy(i, j)
    ax.add_patch(Rectangle((x+0.05, y+0.05), 0.9, 0.9, fc='#F3F3F3', ec='#B8B8C8', hatch='////', lw=0.8, zorder=3, alpha=1.0))
    ax.text(x+0.5, y+0.5, '∅', ha='center', va='center', fontsize=20, color=C_SI, zorder=6)
    ax.text(x+0.5, y+0.17, KEY[i][j].replace('\n',' '), fontsize=6, color=MUTED, ha='center', va='center', zorder=6)
    num(ax, x+0.85, y+0.85, n, C_SI)

def naturalization(ax, a, n, target='S1'):
    i, j = a; x, y = cell_xy(i, j)
    ax.add_patch(Rectangle((x+0.05, y+0.05), 0.9, 0.9, fc='none', ec=C_NA, lw=2.2, zorder=5))
    ax.add_patch(Rectangle((x+0.05, y+0.05), 0.9, 0.9, fc='none', ec=C_NA, hatch='\\\\\\', lw=0, zorder=4, alpha=0.35))
    ax.text(x+0.42, y+0.66, '↓' + target, ha='center', va='center', fontsize=10, color=C_NA, zorder=6, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.15', fc='white', ec=C_NA, lw=1))
    num(ax, x+0.85, y+0.85, n, C_NA)

def revelation(ax, a, n):
    i, j = a; x, y = cell_xy(i, j)
    ax.add_patch(Rectangle((x+0.05, y+0.05), 0.9, 0.9, fc='none', ec=C_RE, lw=2.2, ls=(0, (1.5, 1.5)), zorder=5))
    ax.text(x+0.5, y+0.55, '✦', ha='center', va='center', fontsize=20, color=C_RE, zorder=6)
    ax.add_patch(FancyArrowPatch((x+0.18, y+0.08), (x+0.18, y+0.42), arrowstyle='-|>', mutation_scale=11, color=C_RE, lw=1.6, zorder=6))
    num(ax, x+0.85, y+0.85, n, C_RE)

def legend(ax):
    items = [(C_TR, '⇒ translation: the question is answered with another cell\'s answer'),
             (C_FU, '⊕ fusion: two cells become one question'),
             (C_NA, '↓S1 naturalization: closed within the subsystem, "resolved by nature"'),
             (C_SI, '∅ silencing: the cell is declared nonexistent'),
             (C_RE, '✦ revelation: a closed cell is reopened from below'),
             (INK, 'thick frame: gravity cell (maximal ω)   ·   shading: ω, light → dark   ·   ①② order in the chain, on the source cell')]
    y = -0.2
    for c, t in items:
        ax.text(-1.62, y, '■', color=c, fontsize=7, va='center'); ax.text(-1.45, y, t, fontsize=6.6, color=INK, va='center')
        y -= 0.16

# ---------- Fig. 3: two panels ----------
fig, axes = plt.subplots(1, 2, figsize=(12, 6.6), dpi=250)
fasc = FAM[4]; fem = FAM[8]
draw_grid(axes[0], fasc[1], 'Fig. 3a · Fascism\nchain: ① (2,1)⊕(3,3)   ② (1,2)⇒(2,3)   ③ ∅(4,4)   ④ (3,1)↓S1', ([(1,0),(2,2)]))
fusion(axes[0], (1,0), (2,2), 1); translation(axes[0], (0,1), (1,2), 2); silencing(axes[0], (3,3), 3); naturalization(axes[0], (2,0), 4)
draw_grid(axes[1], fem[1], 'Fig. 3b · Feminisms\nchain: ① ✦(3,1)   ② ✦(2,1)   — no ω of its own: composes with a host', ([(2,0)]))
revelation(axes[1], (2,0), 1); revelation(axes[1], (1,0), 2)
legend(axes[0])
axes[1].text(-1.62, -0.2, 'Same two cells, (3,1) and (2,1): closed by ↓S1 in 3a, reopened by ✦ in 3b — the two poles of the operation.', fontsize=6.8, color=INK, va='center', style='italic')
plt.tight_layout(w_pad=2.5)
fig.savefig('./fig3_operators.png', bbox_inches='tight', facecolor='white')
plt.close(fig)

# ---------- Fig. 2: signature map ----------
order = sorted(range(len(FAM)), key=lambda k: (FAM[k][3][0], FAM[k][3][1]))
fig, ax = plt.subplots(figsize=(11, 5.6), dpi=250)
gap = 0.35
for r, k in enumerate(order):
    name, w, ops, grav = FAM[k]
    W = np.array(w, float); W = W/W.sum()
    for i in range(5):
        for j in range(4):
            x = i*(4+gap) + j; y = len(order)-1-r
            ax.add_patch(Rectangle((x, y), 1, 1, fc=cmap(float(min(W[i,j]/0.22, 1.0))), ec='white', lw=0.6))
            g = ops.get((i, j), '')
            if g:
                dark = W[i,j]/0.22 > 0.55
                ax.text(x+0.5, y+0.5, g, ha='center', va='center', fontsize=9 if len(g)==1 else 7, color='white' if dark else INK, fontweight='bold')
            if (i, j) == grav:
                ax.add_patch(Rectangle((x+0.06, y+0.06), 0.88, 0.88, fc='none', ec=INK, lw=1.6))
    ax.text(-0.3, len(order)-1-r+0.5, name, ha='right', va='center', fontsize=8.5, color=INK)
for i in range(5):
    x0 = i*(4+gap)
    ax.text(x0+2, len(order)+0.75, CONF[i], ha='center', va='bottom', fontsize=8.5, color=INK)
    for j in range(4):
        ax.text(x0+j+0.5, len(order)+0.08, f'S{j+1}', ha='center', va='bottom', fontsize=7, color=MUTED)
ax.set_xlim(-3.6, 5*4+4*gap+0.2); ax.set_ylim(-1.4, len(order)+1.4); ax.set_aspect('equal'); ax.axis('off')
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0, 0.22)); sm.set_array([])
cb = fig.colorbar(sm, ax=ax, fraction=0.025, pad=0.01, ticks=[0, 0.1, 0.2]); cb.set_label('ω (share of the hermeneutic budget per cell)', fontsize=7.5); cb.ax.tick_params(labelsize=7)
ax.text(-3.5, -0.55, 'Families ordered by gravity cell (thick frame). Glyphs: ⇒ translation (source cell)  ⊕ fusion  ↓ naturalization  ∅ silencing  ✦ revelation. Accelerationism and degrowth: near-identical ω, opposite sign of transformation.', fontsize=6.8, color=INK, va='top')
fig.savefig('./fig2_signature_map.png', bbox_inches='tight', facecolor='white')
print('ok')

# ---------- Fig. 2 (option 2): ten signature cards ----------
CHAIN = {
 'Liberalism': '(2,3)⇒(3,2); (2,4)⇒(3,2); ∅(3,1)', 'Socialism': '(4,4)⇒(3,2); (2,4)⇒(2,2)', 'Anarchism': '(3,3)⇒(2,2)',
 'Conservatism': '(5,2)⇒(5,4); (3,1)↓S1', 'Fascism': '(1,2)⇒(2,3); ∅(4,4); (3,1)↓S1', 'Nationalisms': '(1,2)⇒(2,3)',
 'Christian democracy': '(1,2)⇒(2,1) [interposition]', 'Ecologism': '(1,2)⇒(1,1); ✦(5,1)', 'Feminisms': '— (pure revelation)',
 'Accelerationism': '∅(5,4); ∅(4,4)  [+ derivative]', 'Degrowth': '∅(5,4); ∅(4,4)  [− derivative]'}
GRAV = {'Liberalism': '(3,2)', 'Socialism': '(1,2)⊕(3,2)', 'Anarchism': '∅(3,3)', 'Conservatism': '(5,4)', 'Fascism': '(2,1)⊕(3,3)',
        'Nationalisms': '(2,3)⊕(2,4)', 'Christian democracy': '(2,1)⊕(4,4)', 'Ecologism': '(1,1)⊕(5,1)', 'Feminisms': '✦(3,1); ✦(2,1)',
        'Accelerationism': '(5,2)', 'Degrowth': '(5,2)'}
fig, axs = plt.subplots(3, 4, figsize=(12, 9.4), dpi=250)
axs = axs.ravel()
for k, (name, w, ops, grav) in enumerate(FAM):
    ax = axs[k]
    W = np.array(w, float); W = W/W.sum()
    for i in range(5):
        for j in range(4):
            x, y = j, 4-i
            ax.add_patch(Rectangle((x, y), 1, 1, fc=cmap(float(min(W[i,j]/0.22, 1.0))), ec='white', lw=1.2))
            g = ops.get((i, j), '')
            if g:
                dark = W[i,j]/0.22 > 0.55
                ax.text(x+0.5, y+0.5, g, ha='center', va='center', fontsize=11 if len(g)==1 else 8, color='white' if dark else INK, fontweight='bold')
    gcells = [grav] + ([(2,2)] if name=='Fascism' else []) + ([(2,1)] if name=='Socialism' else []) + ([(1,3)] if name=='Nationalisms' else []) \
             + ([(3,3)] if name=='Christian democracy' else []) + ([(4,0)] if name=='Ecologism' else []) + ([(1,0)] if name=='Feminisms' else [])
    for (i, j) in gcells:
        ax.add_patch(Rectangle((j+0.07, 4-i+0.07), 0.86, 0.86, fc='none', ec=INK, lw=1.8))
    for j in range(4): ax.text(j+0.5, 5.08, f'S{j+1}', ha='center', va='bottom', fontsize=6.5, color=MUTED)
    for i in range(5): ax.text(-0.12, 4-i+0.5, f'C{i+1}', ha='right', va='center', fontsize=6.5, color=MUTED)
    ax.set_xlim(-0.7, 4.1); ax.set_ylim(-1.75, 5.7); ax.set_aspect('equal'); ax.axis('off')
    ax.text(-0.6, 5.55, name, fontsize=9.5, fontweight='bold', color=INK, va='bottom')
    ax.text(-0.6, -0.35, 'gravity: ' + GRAV[name], fontsize=7, color=INK, va='top')
    ax.text(-0.6, -0.85, 'chain: ' + CHAIN[name], fontsize=7, color=INK, va='top')
ax = axs[11]; ax.axis('off')
ax.text(0.0, 0.95, 'Fig. 2 · Signature cards ⟨ω, chain⟩', fontsize=9.5, fontweight='bold', color=INK, va='top', transform=ax.transAxes)
leg = ['Rows C1–C5: survival, belonging, order,\nmeaning, transformation.',
       'Columns S1–S4: biological, economic,\npolitical, cultural.',
       'Shading: ω, the share of the hermeneutic\nbudget per cell (light → dark).',
       'Thick frame: gravity cell(s).',
       'Glyphs on the cell where the operator\napplies: ⇒ translation (source)  ⊕ fusion\n↓ naturalization  ∅ silencing  ✦ revelation.',
       'Accelerationism and degrowth: the same ω\nand the same silencings — only the sign of\nthe transformation differs.']
y = 0.82
for t in leg:
    ax.text(0.0, y, t, fontsize=7, color=INK, va='top', transform=ax.transAxes, linespacing=1.25); y -= 0.15 if t.count('\n') < 2 else 0.2
plt.tight_layout(h_pad=1.2, w_pad=0.8)
fig.savefig('./fig2_signature_cards.png', bbox_inches='tight', facecolor='white')
print('cards ok')
