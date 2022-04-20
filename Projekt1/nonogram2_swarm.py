import math
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import numpy as np
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt



kot_reg_poz = [[1,1], [3], [5], [5], [1,1], [1,1], [2,2], [3,1], [5]]
kot_reg_pion = [ [2], [4], [8], [4,3], [2,2], [1], [3], [3], [0]]

example_reg_poz = [[2,1], [1,3], [1,2], [3], [4], [1]]
example_reg_pion = [[1], [5], [2], [5], [2,1], [2]]

curr_reg = [kot_reg_poz, kot_reg_pion]





# Yields successive 'n' sized chunks from list 'list_name'
def create_chunks(list_name, n):
    for i in range(0, len(list_name), n):
        yield list_name[i:i + n]


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
    reg_poz, reg_pion = curr_reg
    dl = len(reg_poz)
    szer = len(reg_pion)
    chunks = list(create_chunks(genes, szer))
    columns = get_columns(chunks)
    # print(len(columns))
    points = 0
    for i in range(len(chunks)):
        row = chunks[i]
        rul_row = check_row(row)
        reg_i_row = reg_poz[i]
        if rul_row == reg_i_row:
            points += 1

    for j in range(len(columns)):
        column = columns[j]
        rul_col = check_column(column)
        reg_j_col = reg_pion[j]
        if rul_col == reg_j_col:
            points += 1

    return points


def f(swarm):
    return [fit(particle)
            for particle in swarm]

options = {'c1': 0.5, 'c2': 0.3, 'w':0.9, 'k':2, 'p':1}

optimizer = ps.discrete.BinaryPSO(n_particles=10, dimensions=15,
options=options)
optimizer.optimize(f, iters=30, verbose=True)
cost_history = optimizer.cost_history
plot_cost_history(cost_history)
plt.show()