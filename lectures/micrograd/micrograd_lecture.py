# %%

import math
import numpy as np
import matplotlib.pyplot as plt

# %%

def f(x):
    return 3*x**2 - 4*x + 5

# %%

f(3.0)

# %%

xs = np.arange(-5, 5, 0.25)
ys = f(xs)
plt.plot(xs, ys)
plt.show()

# %%

h = 0.000001
x = 2/3
(f(x + h) - f(x))/h

# %%

a = 2.0
b = -3.0
c = 10.0
d = a*b + c
print(d)

# %%

h = 0.0001

# inputs
a = 2.0
b = -3.0
c = 10.0

d1 = a*b + c
c += h
d2 = a*b + c

print('d1', d1)
print('d2', d2)
print('slope', (d2 - d1)/h)

# %%

class Value:

    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self._prev = set(_children)
        self._op = _op

    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), '+')
        return out

    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), '*')
        return out

# %%

a = Value(2.0)
b = Value(-3.0)
c = Value(10.0)

d = a*b + c

d._prev
d._op


# %%





# %%






