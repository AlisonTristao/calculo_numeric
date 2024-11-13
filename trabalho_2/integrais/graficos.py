import numpy as np
import matplotlib.pyplot as plt

N = 10
x = np.array([i for i in range(N)], dtype=np.int32)

x2 = np.array([i/100 for i in range(900)], dtype=np.float32)

def equação(x):
    return x**2 + 1

y = equação(x)
y2 = equação(x2)

# plot the data
plt.step(x2, y2, color='gray', linewidth=2, where='post')
plt.scatter(x, y, color='red')
plt.vlines(x, ymin=0, ymax=y, color='gray', linestyle='dotted') 
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xticks(x)
#plt.yticks(y)
plt.grid()

plt.show()
