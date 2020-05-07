import codecademylib
from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)
#create d_bottom and f_bottom here
d_bottom = np.add(Cs , c_bottom)
f_bottom = np.add(d_bottom, Ds)

#create your plot here
plt.figure(figsize=(10,8))
plt.bar(x, As)
plt.bar(x, Bs, bottom = As)
plt.bar(x, Cs, bottom = Ds)
plt.bar(x, Ds, bottom = Fs)
plt.bar(x, Fs)
ax = plt.subplot()
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)
plt.xlabel('Unit')
plt.ylabel('Number of students')
plt.title('Grade Distribution')
plt.savefig('my_stacked_bar.png')


plt.show()