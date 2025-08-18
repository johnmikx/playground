import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 10 * np.pi, 1000)
r = np.sin((8 * theta) / 5)

plt.polar(theta, r)
plt.title('Polar Plot of r = sin(8θ/5)')
plt.show()