import numpy as np
import math

N = 10
x = np.zeros(N)
x[0] = 1
x[1] = 1.5
sum_two = 0

for i in range(2, N):
    x[i] = 0.2 * x[i-1] + 1.2 * x[i-2]

    if 2.0 <= x[i] <= 3.0:
        sum_two = sum_two + x[i]

print(*x, sep="\n")

y = sum(x)
print("The sum of all values is: " + str(y))

print("The sum of values between 2.0 and 3.0 is: " + str(sum_two))
