import numpy as np
import matplotlib.pyplot as plt
# entropy of bornulli distribution
x = np.linspace(0.01,0.99, 101)
print 'x:', x
y = -x * np.log2(x) - (1-x) * np.log2(1-x)
print 'y', y
plt.plot(x,y)
plt.show()
