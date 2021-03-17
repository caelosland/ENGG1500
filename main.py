import numpy as np
import matplotlib.pyplot as plt
import math

t = np.linspace(0, math.pi, 500)

y = 2 * np.sin((5 * t) + math.pi)

plt.plot(t, y)
plt.title('Oscillation One Vs. Time')  # add title
plt.show()

