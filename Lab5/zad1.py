import math
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import numpy as np
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt



def endurance2(x, y, z, u, v, w):
    return math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w)

def endurance(args):
    return endurance2(*args)

def f(swarm):
    return [(-1) * endurance(particle)
            for particle in swarm]

options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
x_min = np.zeros(6)
x_max = np.ones(6)
my_bounds = (x_min, x_max)

optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6,
options=options, bounds=my_bounds)
stats = optimizer.optimize(f, iters=1000)





best_cost, best_pos = stats
print(f"best cost: {best_cost}, best pos: {best_pos}")

cost_history = optimizer.cost_history
plot_cost_history(cost_history)
plt.show()