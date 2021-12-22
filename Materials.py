import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

Materials = pd.read_excel(r'/Users/macbookpro/Desktop/New Technologies/Copy of Materials Data.xlsx')

fonttype = {'fontname': 'Times New Roman'}
colors = {'Polyurethane':'cyan', 'Silicone':'deepskyblue', 'TPE':'red'}

fig = plt.figure()
ax1 = fig.add_subplot(133)
plt.scatter('Mat.', 'Compress. Elasticity (kPa)',  data=Materials,  c=Materials['Mat.'].map(colors), marker='_')
ax1.set_xlabel('',fontsize=12, **fonttype)
ax1.set_ylabel('Compressive Elasticity (kPa)',fontsize=12, **fonttype)
for tick in ax1.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Times New Roman")
sns.despine()

ax2 = fig.add_subplot(132)
plt.scatter('Mat.', 'Tensile Elasticity (kPa)',  data=Materials,c=Materials['Mat.'].map(colors),marker='_')
ax2.set_ylabel('Tensile Elasticity (kPa)',fontsize=12, **fonttype)
ax2.set_xlabel('',fontsize=12, **fonttype)
for tick in ax2.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax2.get_yticklabels():
    tick.set_fontname("Times New Roman")
sns.despine()

ax3 = fig.add_subplot(131)
plt.scatter('Mat.', 'Coeff. Of Friction (N/N)',  data=Materials,c=Materials['Mat.'].map(colors),marker='_')
ax3.set_ylabel('Coefficient Of Friction (N/N)',fontsize=12, **fonttype)
ax3.set_xlabel('',fontsize=12, **fonttype)
for tick in ax3.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax3.get_yticklabels():
    tick.set_fontname("Times New Roman")
sns.despine()
plt.tight_layout(pad=1.5)
plt.show()


