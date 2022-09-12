import random

# Specifying the cites on a array
# Cities: A, B, C, D, E
# 0 represents the cities distance to itself,

cities = [[0, 2, 6, 3, 6],
          [2, 0, 4, 3, 7],
          [6, 4, 0, 7, 3],
          [3, 3, 7, 0, 3],
          [6, 7, 3, 3, 0]]

A = 0
B = 1
C = 2
D = 3
E = 4

# Fitness is multiplied by -1 because it makes the
# smallest number the biggest
def calcFitness(list):
    fitness = 0
    for i in range (1, len(list)):        
        fitness += cities[i-1, i]
    
    return fitness * -1


def dnaGenerate():
    list = [A, B, C, D, E]
    random.shuffle(list)
    return list

def populationGenerate(size):
    population = dnaGenerate()
    for i in range(size-1):
        population.append(dnaGenerate())

    return population

def selectTwoRoutes(population):
    parents = [population[1], population[0]]
    for i in range(2, len(population)):
        if (calcFitness(population[i]) > calcFitness(parents[0])):
            parents[0] = population[i]
        elif (calcFitness(population[i]) > calcFitness(parents[1])):
            parents[1] = population[i]
    
    return parents

    

def crossover(parents):
    aux1 = random.randint(0,len(parents))
    aux2 = random.randint(0,len(parents))
    
    child = [0,0,0,0,0]

    for i in range(aux2):
        child[aux1] = parents[0][aux1]
        if(aux1 == 4):
            aux1 == 0




    
