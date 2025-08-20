import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100)

sns.violinplot(data=data, inner=None, color='lightgray')
sns.swarmplot(data=data, color='blue', alpha=0.5)
plt.title('Violin Swarm Plot', fontweight='bold')
plt.show()