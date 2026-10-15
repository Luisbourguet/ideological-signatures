import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
INK='#1F1F2E'; MUTED='#6B6B80'
fig,ax=plt.subplots(figsize=(9,6.4),dpi=250); ax.set_xlim(0,10); ax.set_ylim(0,10.3); ax.axis('off')
strata=[(4,'Stratum 4 · Ideological crystallizations','belief fields I = ⟨C, S, D, G, B, A, P, V, I, O, M⟩; signature ⟨ω, chain⟩;\nconcrete formations and their carriers','#F6E3DC','#C8521E'),
        (3,'Stratum 3 · Four social subsystems S1–S4','biological, economic, political, cultural; technology as transversal product','#E3EFD9','#5A7D2A'),
        (2,'Stratum 2 · Durable symbolic forms','rites, institutions, artifacts — the stratum that hosts the matrix','#E6E4F7','#4A41A8'),
        (1,'Stratum 1 · Five existential conflicts C1–C5','survival, belonging, order, meaning, transformation','#DDE9F5','#1F6FB2'),
        (0,'Stratum 0 · Realist-emergentist principle','symbolic reality emerges from the world to thought; the analyst recognizes it','#EDEDED','#6B6B80')]
ys={4:8.35,3:6.85,2:4.05,1:2.15,0:0.65}; h={4:1.3,3:1.15,2:2.45,1:1.15,0:1.15}
for k,t,sub,fc,ec in strata:
    y=ys[k]; ax.add_patch(FancyBboxPatch((0.4,y),6.6,h[k],boxstyle='round,pad=0.02,rounding_size=0.12',fc=fc,ec=ec,lw=1.2))
    ax.text(0.65,y+h[k]-0.32,t,fontsize=9.5,fontweight='bold',color=INK,va='top')
    ax.text(0.65,y+h[k]-0.72,sub,fontsize=7.6,color=INK,va='top',wrap=True)
# matrix inside stratum 2
mx,my=1.0,ys[2]+0.22
for i in range(5):
    for j in range(4):
        ax.add_patch(FancyBboxPatch((mx+j*0.42,my+i*0.19),0.38,0.16,boxstyle='square,pad=0',fc='white',ec='#AFA9EC',lw=0.6))
ax.text(mx+2.0,my+0.5,'M = C × S\n(5 conflicts × 4 subsystems)\nω: bounded weighting over the cells\nsix operators ⇒ ⊕ ↓ ∅ ✦ ∥',fontsize=7.4,color=INK,va='center')
# arrows: vertical reading
for (y0,y1,txt) in [(ys[1]+h[1],ys[2],'conflicts are thematized by symbolic forms'),(ys[2]+h[2],ys[3],'…and distributed over the subsystems'),(ys[3]+h[3],ys[4],'…ideology is the resulting selection and weighting')]:
    ax.add_patch(FancyArrowPatch((3.7,y0),(3.7,y1),arrowstyle='-|>',mutation_scale=12,color=MUTED,lw=1.2))
    ax.text(3.85,(y0+y1)/2,txt,fontsize=7,color=MUTED,va='center')
# right column: Epstein roles
ax.text(7.45,9.95,'Role in the account',fontsize=8.5,fontweight='bold',color=INK,va='top')
roles=[(ys[4]+h[4]/2-0.15,'GROUNDS\nwhat makes this formation\nthe ideology it is: ⟨ω, chain⟩\n(emergent powers live here)'),
       ((ys[3]+h[3]/2+ys[2]+h[2]/2)/2,'FRAME PRINCIPLES\nstrata 1–3: how any\nideological fact is grounded\n(nested frames, no new entities)'),
       (ys[1]+h[1]/2,''),
       (ys[0]+h[0]/2,'ANCHOR of the frame\nheld fallibly, as a\nworking hypothesis')]
for y,t in roles:
    if t: ax.text(7.45,y,t,fontsize=7.4,color=INK,va='center',linespacing=1.3)
ax.add_patch(FancyBboxPatch((7.25,ys[1]-0.05),2.6,ys[3]+h[3]-ys[1]+0.1,boxstyle='round,pad=0.02,rounding_size=0.1',fc='none',ec='#B8B8C8',lw=0.8,ls='--'))
ax.text(7.45,ys[1]+h[1]/2,'ANCHORS of family membership:\nlineage and replication (C, S)\n— a historical question',fontsize=7.4,color=INK,va='center',linespacing=1.3)
ax.text(0.4,0.25,'Fig. 1 · The five-strata architecture and the role of each stratum (frame / grounds / anchors, after Epstein 2015).',fontsize=7.6,color=MUTED,va='top')
fig.savefig('./fig1_strata.png',bbox_inches='tight',facecolor='white'); print('fig1 ok')
