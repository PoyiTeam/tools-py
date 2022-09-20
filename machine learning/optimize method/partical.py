# %%

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


INF = 1e5


def plot_cost_func():
    """畫出適應度函式"""
    fig = plt.figure()
    ax = Axes3D(fig)
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 0.25)
    X, Y = np.meshgrid(X, Y)
    Z = (X**2 + Y**2) - 10
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
    plt.show()


def fitness(x):
    return (x[0]-2)**4 + (x[0]-2*x[1])**2


class PSOSolver(object):
    def __init__(self, n_iter, weight=0.5, c1=2, c2=2, n_particle=5):
        self.n_iter = n_iter
        self.weight = weight
        self.c1 = c1
        self.c2 = c2
        self.n_particle = n_particle
        self.gbest = np.random.rand(2)
        # gbest 對應的函式值
        self.gbest_fit = fitness(self.gbest)
        # 將位置初始化到 [-5,5]
        self.location = 4 * np.random.rand(n_particle, 2) - 2
        # 將速度初始化到 [-0.5,0.5]
        self.velocity = np.random.rand(n_particle, 2) - 0.5
        self.pbest_fit = np.tile(INF, n_particle)
        self.pbest = np.zeros((n_particle, 2))
        # 記錄每一步的最優值
        self.best_fitness = []

    def new_velocity(self, i):
        r = np.random.rand(2, 2)
        v = self.velocity[i]
        x = self.location[i]
        pbest = self.pbest[i]
        return self.weight * v + self.c1 * r[0] * (pbest - x) + \
            self.c2 * r[1] * (self.gbest - x)

    def solve(self):
        for it in range(self.n_iter):
            for i in range(self.n_particle):
                v = self.new_velocity(i)
                x = self.location[i] + v
                fit_i = fitness(x)
                if fit_i < self.pbest_fit[i]:
                    self.pbest_fit[i] = fit_i
                    self.pbest[i] = x
                    if fit_i < self.gbest_fit:
                        self.gbest_fit = fit_i
                        self.gbest = x
                self.velocity[i] = v
                self.location[i] = x
            self.best_fitness.append(self.gbest_fit)


if __name__ == '__main__':
    plot_cost_func()
    n_iter = 100
    s = PSOSolver(n_iter, weight=0.5, c1=1, c2=1, n_particle=5)
    s.solve()
    print(s.gbest_fit)
    plt.title("Fitness Curve")
    plt.xlabel("iter")
    plt.ylabel("fitness")
    plt.plot(np.arange(n_iter), np.array(s.best_fitness))
    plt.show()
