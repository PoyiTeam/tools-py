"""
referenc
https://oemiliatano.github.io/2021/03/01/%E6%9C%80%E4%BD%B3%E5%8C%96-%E7%89%9B%E9%A0%93%E6%B3%95/
"""

# %%
import numpy as np
import matplotlib.pyplot as plt


def f(x, y): return (x-2)**4 + (x-2*y)**2

# define diff function


def dfdx(x0, y0):
    h = 1e-5
    return (f(x0 + h, y0) - f(x0, y0)) / h


def dfdy(x0, y0):
    h = 1e-5
    return (f(x0, y0 + h) - f(x0, y0)) / h


def dfdxdx(x0, y0):
    g = 1e-5
    return (dfdx(x0 + g, y0) - dfdx(x0, y0)) / g


def dfdxdy(x0, y0):
    g = 1e-5
    return (dfdx(x0, y0 + g) - dfdx(x0, y0)) / g


def dfdydy(x0, y0):
    g = 1e-5
    return (dfdy(x0, y0 + g) - dfdy(x0, y0)) / g


def H(x0, y0):
    """ Hessian matrix """
    h = [[dfdxdx(x0, y0), dfdxdy(x0, y0)], [dfdxdy(x0, y0), dfdydy(x0, y0)]]
    return h


def grd(x0, y0):
    """ gradient matrix """
    return [dfdx(x0, y0), dfdy(x0, y0)]


# %%
# initial value
#x0 = 0
#y0 = 3
x0 = np.random.uniform(-2, 2)
y0 = np.random.uniform(-2, 2)

# Hessian inverse matrix * gradient matrix
k = -np.linalg.solve(H(x0, y0), grd(x0, y0))

# 1st iteration
x1 = x0 + k[0]
y1 = y0 + k[1]

# plot contour
X = np.linspace(-3, 3, 1024)
Y = np.linspace(-3, 3, 1024)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)
C = plt.contour(X, Y, Z, 50)
plt.xlabel("x")
plt.ylabel("y")
plt.clabel(C, inline=True)
plt.plot((x0, x1), (y0, y1), 'bo-')

# learning parameters
tolerance = 0.07
lr = 0.01  # learning rate
epoch = 0

# start learning
while f(x0, y0) > tolerance:
    epoch += 1
    x0 = x1
    y0 = y1
    k = -np.linalg.solve(H(x0, y0), grd(x0, y0))
    x1 = x0 + lr * k[0]
    y1 = y0 + lr * k[1]
    print(f"{epoch} epoch - x:{x1:.3f}, y:{y1:.3f}")
    print(f"output:{f(x0, y0):.3f}", )
    plt.plot((x0, x1), (y0, y1), 'ro-')

plt.plot(x0, y0, 'y*')

print(f"root x, y: {x0:.3f}, {y0:.3f}")
print(f"output:{f(x0, y0):.3f}", )
