import matplotlib.pyplot as plt
import pandas as pd

# csv第一行换成     index,gene,chromosome,pvalue
df = pd.read_csv('hh.csv', usecols=['gene', 'chromosome', 'pvalue'])
df['minuslog10pvalue'] = -np.log10(df.pvalue)
df = df.sort_values('chromosome')
df['ind'] = range(len(df))
df_grouped = df.groupby(('chromosome'))

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
colors = ['red','green','blue', 'yellow']
x_labels = []
x_labels_pos = []
for num, (name, group) in enumerate(df_grouped):
    group.plot(kind='scatter', x='ind', y='minuslog10pvalue',color=colors[num % len(colors)], ax=ax)
    x_labels.append(name)
    x_labels_pos.append((group['ind'].iloc[-1] - (group['ind'].iloc[-1] - group['ind'].iloc[0])/2))
ax.set_xticks(range(0,300,20))
# ax.set_xticklabels(x_labels)
ax.set_xlim([0, len(df)])
ax.set_ylim([0, 3.5])
ax.set_xlabel('Chromosome')