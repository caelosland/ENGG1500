# Task 3
import numpy as np

N = 10
x = np.zeros(N)
x[0] = 1
i = 1
sum_two = 0

while i < N:
    x[i] = 0.8 * x[i-1] + 1
    if 2.0 <= x[i] <= 3.0:
        sum_two = sum_two + x[i]
    i = i + 1


print(*x, sep="\n")

y = sum(x)
print("The sum of all values is: " + str(y))

print("The sum of values between 2.0 and 3.0 is: " + str(sum_two))

