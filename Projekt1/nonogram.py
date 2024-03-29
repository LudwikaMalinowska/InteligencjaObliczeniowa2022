import pygad
import numpy

kot_reg_poz = [[1,1], [3], [5], [5], [1,1], [1,1], [2,2], [3,1], [5]]
kot_reg_pion = [ [2], [4], [8], [4,3], [2,2], [1], [3], [3]]

lemur_reg_poz = [[1,1], [2,2], [5], [2,1,2,1], [5,2], [3,1], [6,2], [1,5,1],
                 [8], [2,4]]
lemur_reg_pion = [[1,2], [4,1,1], [3,6], [7], [3,6], [4,4], [1,3], [2], [3,1],
                  [2,3]]

rabbit_reg_poz = [[2], [1,1], [3], [1,2], [8], [9], [9], [7], [3,3], [3,4]]
rabbit_reg_pion = [[1,3,1], [3,2], [9], [1,7], [2,4,1], [4,1], [6],
                   [6], [4], [1]]

example_reg_poz = [[2,1], [1,3], [1,2], [3], [4], [1]]
example_reg_pion = [[1], [5], [2], [5], [2,1], [2]]

gene_space = [0,1]
sol_per_pop = 1000
num_parents_mating = 500
num_generations = 100
keep_parents = 50
# sol_per_pop = 10
# num_parents_mating = 2
# num_generations = 2
# keep_parents = 2
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 4

# curr_reg = [kot_reg_poz, kot_reg_pion]
curr_reg = [example_reg_poz, example_reg_pion]


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


def fit(genes, solution_idx):
    reg_poz, reg_pion = curr_reg
    dl = len(reg_poz)
    szer = len(reg_pion)
    chunks = list(create_chunks(genes, szer))
    columns = get_columns(chunks)
    # print(len(columns))
    points = 0
    for i in range(len(chunks)):
        for j in range(len(columns)):
            row = chunks[i]
            column = columns[j]
            rul_col = check_row(row)
            rul_row = check_column(column)

            reg_i_row = reg_poz[i]
            reg_j_col = reg_pion[j]

            if rul_row == reg_i_row and rul_col == reg_j_col:
                # print(f"i: {i}, j: {j}, reg_row: {reg_i_row}, reg_col: {reg_j_col}")
                points += 5
            elif rul_row == reg_i_row or rul_col == reg_j_col:
                points += 1
            # elif (sum(rul_row) == sum(reg_i_row)) or (sum(rul_col) == sum(reg_j_col)):
            #     points += 3
            # else:
            #     # try:
            #         sum1row = sum(rul_row)
            #         sum2row = sum(reg_i_row)
            #
            #         sum1col = sum(rul_col)
            #         sum2col = sum(reg_j_col)
            #
            #         if (sum1row == sum2row) or (sum1col == sum2col):
            #             points += 3

                # except (TypeError):
                #     print("err:", rul_col, reg_j_col)
                #     # raise TypeError


            # if (i == 0):
            #     print(rul_col, reg_j_col)

    # for i in range(len(columns)):
    #     column = columns[i]
    #     rul = check_column(column)
    #     reg_i = reg_pion[i]
    #     if rul == reg_i:
    #         points += 5

    return points



def run(reg):
    reg_poz, reg_pion = reg
    dl = len(reg_pion)
    szer = len(reg_poz)
    num_genes = dl * szer
    fitness_function = fit

    # inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
    ga_instance = pygad.GA(gene_space=gene_space,
                           num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_function,
                           sol_per_pop=sol_per_pop,
                           num_genes=num_genes,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes)

    # uruchomienie algorytmu
    ga_instance.run()

    # podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    chunks = list(create_chunks(solution, szer))
    sum_chunks = list([sum(chunk) for chunk in chunks])
    print("Parameters of the best solution : ")
    for chunk in chunks:
        print(chunk)
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

    # wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
    ga_instance.plot_fitness()


run(curr_reg)

c = [
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6]
]

# print(get_columns(c))

# print(sum([5]))