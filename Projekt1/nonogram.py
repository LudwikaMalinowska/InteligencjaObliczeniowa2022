import pygad
import numpy

kot_reg_poz = [[1,1], [3], [5], [5], [1,1], [1,1], [2,2], [3,1], 5]
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
sol_per_pop = 10
num_parents_mating = 5
num_generations = 30
keep_parents = 2
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 10

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
    return rul

def fit(genes, solution_idx):
    reg_poz, reg_pion = curr_reg
    dl = len(reg_pion)
    szer = len(reg_poz)
    chunks = list(create_chunks(genes, szer))

    points = 0
    for i in range (len(chunks)):
        row = chunks[i]
        rul = check_row(row)
        reg_i = reg_poz[i]
        if rul == reg_i:
            points += 5

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
    print("Parameters of the best solution : {solution}".format(solution=chunks))
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))



run(curr_reg)
