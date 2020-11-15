import numpy as np 
import matplotlib as plt 

x = np.arange(o., 10.0, 0.2)

plt.plot(x, x**2 + 2, 'g--')
plt.plot(x, x**3, 'r^')
plt.plot(x, x*4 - 3, 'b')
plt.xlabel("my inputs")
plt.ylabel('my outputs')
plt.title('my graph')
plt.show()