import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.functions.single_obj import sphere
from pyswarms.utils.plotters import plot_cost_history
from matplotlib import pyplot as plt

import pyswarms.backend as P
from pyswarms.backend.swarms import Swarm
from pyswarms.backend.topology.ring import Ring
from pyswarms.backend.topology.von_neumann import VonNeumann
import numpy as np



# Set-up hyperparameters
# options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
# my_topology = Star()
# my_swarm = P.create_swarm(n_particles=50, dimensions=2, options=options)
# print(my_swarm.options.items())
# Call instance of GlobalBestPSO
# optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2,
#                                     options=options)

# best_pos, best_cost = my_topology.compute_gbest(my_swarm)
# Perform optimization
# stats = optimizer.optimize(fx.sphere, iters=100)


# Obtain cost history from optimizer instance
# cost_history = optimizer.cost_history

# Plot!
# plot_cost_history(cost_history)
# plt.show()
#
# print(cost_history)

# my_topology = Ring() # The Topology Class
my_topology = VonNeumann()
# my_options = {'c1': 0.6, 'c2': 0.3, 'w': 0.4}  # arbitrarily set
my_options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
my_swarm = P.create_swarm(n_particles=50, dimensions=2, options=my_options)
print('The following are the attributes of our swarm: {}'.format(my_swarm.__dict__.keys()))


iterations = 100  # Set 100 iterations
for i in range(iterations):
    # Part 1: Update personal best
    my_swarm.current_cost = sphere(my_swarm.position)  # Compute current cost
    my_swarm.pbest_cost = sphere(my_swarm.pbest_pos)  # Compute personal best pos
    my_swarm.pbest_pos, my_swarm.pbest_cost = P.compute_pbest(my_swarm)  # Update
    # ˓→ and store
    # Part 2: Update global best
    # Note that gbest computation is dependent on your topology
    if np.min(my_swarm.pbest_cost) < my_swarm.best_cost:
        # my_swarm.best_pos, my_swarm.best_cost = my_topology.compute_gbest(my_swarm, p=2, k=2)
        my_swarm.best_pos, my_swarm.best_cost = my_topology.compute_gbest(my_swarm, p=2, r=4)
        # max 4: r*r + (r+1)(r+1)
    # Let's print our output

    if i % 20 == 0:
        print('Iteration: {} | my_swarm.best_cost: {:.4f}'.format(i + 1, my_swarm.best_cost))
    # Part 3: Update position and velocity matrices
    # Note that position and velocity updates are dependent on your topology
    my_swarm.velocity = my_topology.compute_velocity(my_swarm)
    my_swarm.position = my_topology.compute_position(my_swarm)
print('The best cost found by our swarm is: {:.4f}'.format(my_swarm.best_cost))
print('The best position found by our swarm is: {}'.format(my_swarm.best_pos))
