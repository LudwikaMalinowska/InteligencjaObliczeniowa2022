import math
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import numpy as np
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt

from Projekt1.image import plot

kot_reg_poz = [[1,1], [3], [5], [5], [1,1], [1,1], [2,2], [3,1], [5]]
kot_reg_pion = [ [2], [4], [8], [4,3], [2,2], [1], [3], [3]]

example_reg_poz = [[2,1], [1,3], [1,2], [3], [4], [1]]
example_reg_pion = [[1], [5], [2], [5], [2,1], [2]]

# example_reg_poz = [[1], [2], [3], [4], [5]]
# example_reg_pion = [[5], [4], [3], [2], [1]]
#
pyramid2_reg_poz = [[1], [2], [3], [4], [5], [6]]
pyramid2_reg_pion = [[6], [5], [4], [3], [2], [1]]

pyramid3_reg_poz = [[5], [3], [1], [1], [3], [5]]
pyramid3_reg_pion = [[1], [1,2], [2,3], [3,2], [2,1], [1]]

pyramid4_reg_poz = [[7], [5], [3], [1], [3], [5], [7]]
pyramid4_reg_pion = [[1,1], [2,2], [3,3], [7], [3,3], [1,1]]

ant_reg_poz = [[1,1,1,1], [1,1,1,1], [1,1,1], [3], [1], [3],
               [5], [1,1], [1,1]]
ant_reg_pion = [[2,2], [1,1], [2,1,2], [6], [2,1,2], [1,1],
                [2,2]]

# curr_reg = [example_reg_poz, example_reg_pion]
curr_reg = [kot_reg_poz, kot_reg_pion]

flat_list = [item for sublist in curr_reg[1] for item in sublist]
black = sum(flat_list)





# Yields successive 'n' sized chunks from list 'list_name'
def create_chunks(list_name, n):
    for i in range(0, len(list_name), n):
        yield list_name[i:i + n]

def print_sol(sol):
    chunks = create_chunks(sol, len(curr_reg[0]))

    lst = []
    for row in chunks:
        print(row)
        lst.append(row)

    print(lst)
    plot(lst)

def check_row(row):
    length = 0
    rul = []
    for gene in row:
        if gene == 1:
            length += 1
        elif length != 0 and gene == 0:
            rul.append(length)
            length = 0

    if length != 0:
        rul.append(length)

    return rul

def check_column(column):
    length = 0
    rul = []
    for gene in column:
        if gene == 1:
            length += 1
        elif length != 0 and gene == 0:
            rul.append(length)
            length = 0

    if length != 0:
        rul.append(length)

    return rul

#działa
def get_columns(chunks):
    columns = []
    for i in range(len(chunks[0])):
        col = []
        for j in range(len(chunks)):
            col.append(chunks[j][i])
        columns.append(col)
    # print("columns", columns)
    return columns


def fit(genes):
    # print("genes: ", genes)
    reg_poz, reg_pion = curr_reg
    dl = len(reg_poz)
    szer = len(reg_pion)

    flat_list = [item for sublist in reg_pion for item in sublist]
    black = sum(flat_list)
    count = sum(genes)
    points = 0.0
    points -= abs(black - count) * 2.0


    chunks = list(create_chunks(genes, szer))
    columns = get_columns(chunks)
    # print(len(columns))

    for i in range(len(chunks)):
        row = chunks[i]
        rul_row = check_row(row)
        reg_i_row = reg_poz[i]
        if rul_row == reg_i_row:
            points += 1.0
        else:
            points -= 0.5

    for j in range(len(columns)):
        column = columns[j]
        rul_col = check_column(column)
        reg_j_col = reg_pion[j]
        if rul_col == reg_j_col:
            points += 1.0
        else:
            points -= 0.5

    return points


def f(swarm):
    return [(-1) * fit(particle)
            for particle in swarm]

options = {'c1': 0.5, 'c2': 0.3, 'w':0.9, 'k':2, 'p':1}

n_genes = len(curr_reg[0]) * len(curr_reg[1])
print(n_genes)
optimizer = ps.discrete.BinaryPSO(n_particles=10, dimensions=n_genes,
options=options)
best_cost, best_pos = optimizer.optimize(f, iters=300000, verbose=True)
cost_history = optimizer.cost_history
plot_cost_history(cost_history)
plt.show()

print_sol(best_pos)