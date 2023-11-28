# =================================================================================================
# Author:                   Austin Purvis
# Email Addresse:           atpu225@uky.edu
# Date:                     11/27/23
# Purpose:                  Implements the composite simpson method. Further description below.
# =================================================================================================

import numpy as np

def simpson_composite(f, a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        
        if i%2 == 1:
            result = result + 4*f(x)
        else:
            result = result + 2*f(x)

    result = result * h / 3

    return result

def f(x):
    return x * np.log(x)

# Define the interval [a, b] and the number of iterations (n)
a = 1
b = 2
n = 4

# Compute the Romberg array
result = simpson_composite(f, a, b, n)

# Display the result
print("Result:")
print(result)