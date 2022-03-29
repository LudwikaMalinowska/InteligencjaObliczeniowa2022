import math
import pygad
import numpy
import time






labirynt = [
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,2,0,0,1,0,0,0,1,0,0,1],
    [1,1,1,0,0,0,1,0,1,1,0,1],
    [1,0,0,0,1,0,1,0,0,0,0,1],
    [1,0,1,0,1,1,0,0,1,1,0,1],
    [1,0,0,1,1,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,1,0,0,0,1,1],
    [1,0,1,0,0,1,1,0,1,0,0,1],
    [1,0,1,1,1,0,0,0,1,1,0,1],
    [1,0,1,0,1,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,3,1],
    [1,1,1,1,1,1,1,1,1,1,1,1]
]

#0 - prawo, 1 - lewo, 2 - góra, 3 - dół
steps_dict = {
    0: "Prawo",
    1: "Lewo",
    2: "Góra",
    3: "Dół"
}

#definiujemy parametry chromosomu
#geny to liczby: 0 lub 1
gene_space = [0, 1, 2, 3]
# gene_space = {"low": 0, "high": 1, "step": 0.01}




def filter_steps(steps):
    curr = {"x": 1, "y": 1}
    filtered_steps = []
    for i in range(len(steps)):
        step = steps[i]
        if step == "Prawo":
            nField = {"x": curr["x"], "y": curr["y"] + 1}
        elif step == "Lewo":
            nField = {"x": curr["x"], "y": curr["y"] - 1}
        elif step == "Góra":
            nField = {"x": curr["x"] - 1, "y": curr["y"]}
        else:
            nField = {"x": curr["x"] + 1, "y": curr["y"]}

        nextField = labirynt[nField["x"]][nField["y"]]
        if nextField == 0:
            curr = nField
            filtered_steps.append(step)
        elif nextField == 3:
            filtered_steps.append(step)
            break

    return filtered_steps

def count_stop(steps):
    extra_points = 0
    curr = {"x": 1, "y":1}
    for i in range(len(steps)):
        step = steps[i]
        if step == 0 :
            nField = {"x": curr["x"], "y": curr["y"] + 1}
        elif step == 1 :
            nField = {"x": curr["x"], "y": curr["y"] - 1}
        elif step == 2 :
            nField = {"x": curr["x"] - 1, "y": curr["y"]}
        else:
            nField = {"x": curr["x"] + 1, "y": curr["y"]}

        nextField = labirynt[nField["x"]][nField["y"]]

        if nField == curr:
            extra_points -= 0.2

        if nextField == 0:
            curr = nField
        elif nextField == 3:
            curr = nField
            extra_points += (len(steps) - i)
            break


    return curr, extra_points

#definiujemy funkcjÄ fitness
def fitness_func(solution, solution_idx):
    stop, extra_points= count_stop(solution)
    end = {"x": 10, "y": 10}
    odl = (-1) * (abs(stop["x"] - end["x"]) + abs(stop["y"] - end["y"]))

    if odl == 0:
        return odl + extra_points + 10
    else:
        return odl + extra_points

fitness_function = fitness_func

#ile chromsomĂłw w populacji
#ile genow ma chromosom
sol_per_pop = 20
num_genes = 30

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 10
num_generations = 100
keep_parents = 4

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 5

#inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
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
                       mutation_percent_genes=mutation_percent_genes,
                       # stop_criteria=["reach_15"]
                       )

start = time.time()
#uruchomienie algorytmu
ga_instance.run()

end = time.time()
print(end - start)


#podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
solution = list(map(lambda x: steps_dict[x], solution))
fsolution = filter_steps(solution)
print("Parameters of the best solution : {solution}".format(solution=solution))
print(f"Filtered solution : {fsolution}")
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

#tutaj dodatkowo wyswietlamy sume wskazana przez jedynki
# prediction = numpy.sum(solution)
# print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

#wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()