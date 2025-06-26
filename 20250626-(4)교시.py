# 시각화
# -matplotlib.pyplot
# -seaborn
# -pandas의 시각화
import seaborn as sns
import pandas as pd
import numpy as np

anscombe = sns.load_dataset("anscombe")
print(anscombe)

ans = sns.load_dataset("anscombe")
ans
dataset_1 = ans[ans['dataset'] == 'I']
dataset_2 = ans[ans['dataset'] == 'II']
dataset_3 = ans[ans['dataset'] == 'III']
dataset_4 = ans[ans['dataset'] == 'IV']


import matplotlib.pyplot as plt
plt.plot(dataset_1['x'],dataset_1['y'],'ro')
plt.plot(dataset_2['x'],dataset_2['y'],'o')
plt.plot(dataset_3['x'],dataset_3['y'],'o')
plt.plot([0,1],[10,20],'ro')

fig = plt.figure()
axes1 = fig.add_subplot(2,2,1)
axes2 = fig.add_subplot(2,2,2)
axes3 = fig.add_subplot(2,2,3)
axes4 = fig.add_subplot(2,2,4)


axes1.plot(dataset_1['x'],dataset_1['y'],'o')
axes2.plot(dataset_2['x'],dataset_2['y'],'o')
axes3.plot(dataset_3['x'],dataset_3['y'],'o')
axes4.plot(dataset_4['x'],dataset_4['y'],'o')
fig.suptitle("Title")
axes1.set_title("No1")
axes2.set_title("No2")
axes3.set_title("No3")
axes4.set_title("No4")

fig, axes = plt.subplots(2,2,figsize=(8,2))


axes[0][0].plot(dataset_1['x'],dataset_1['y'],'o')
axes[0][0].plot(dataset_2['x'],dataset_2['y'],'o')
axes[0][0].plot(dataset_3['x'],dataset_3['y'],'o')
axes[0][0].plot(dataset_4['x'],dataset_4['y'],'o')
plt.tight_layout()


plt.show()





fig, ax = plt.subplots()

ax.hist(tips['total_bill'], bins=8, linewidth=0.5, edgecolor="white")

plt.style.available
plt.style.use('Solarize_Light2')
plt.style.use('tableau-colorblind10')

plt.show()



fig, ax = plt.subplots()
ax.scatter(tips['day'], tips['total_bill'])

plt.show()