import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.fill_between(x, y1, color='skyblue', alpha=0.5)
plt.fill_between(x, y2, color='sandybrown', alpha=0.5)
plt.xlabel('X-axis', fontweight='bold')
plt.ylabel('Y-axis', fontweight='bold')
plt.title('Area Between Two Lines', fontweight='bold')
plt.show()