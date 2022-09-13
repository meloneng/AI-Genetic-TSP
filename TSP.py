import random

# Specifying the cites on a array
# Cities: A, B, C, D, E
# 0 represents the cities distance to itself,


class cityA:
    ind = 0
    dist = [0, 2, 6, 3, 6]

class cityB:
    ind = 1
    dist = [2, 0, 4, 3, 7]

class cityC:
    ind = 2
    dist = [6, 4, 0, 7, 3]

class cityD:
    ind = 3
    dist = [3, 3, 7, 0, 3]

class cityE:
    ind = 4
    dist = [6, 7, 3, 3, 0]

# Fitness is multiplied by -1 because it makes the
# smallest path the biggest score
def calcFitness(dna):
    fitness = 0
    for i in range (1, len(dna)):
        fitness += dna[i].dist[dna[i-1].ind]

    return (fitness * -1)


def dnaGenerate():
    dna = [cityA, cityB, cityC, cityD, cityE]
    random.shuffle(dna)
    return dna

def populationGenerate(size):
    population = []
    population.append(dnaGenerate())
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
    aux1 = random.randint(0,len(parents)-1)
    aux2 = random.randint(0,len(parents)-1)
    
    child = [0,0,0,0,0]

    for i in range(aux2):
        child[aux1] = parents[0][aux1]
        if(aux1 == 4):
            aux1 == 0
            continue
        aux1 += 1

    for i in range(len(parents)):
        if(parents[1][aux1] not in child):
            child[aux1] = parents[1][aux1]
            if(aux1 == 4):
                aux1 == 0
            else:
                aux1 += 1
                continue
        else:
            continue
    
    if((random.randint(0,100) < 4)):
        aux3 = random.randint(0, len(child)-1)
        aux4 = random.randint(0, len(child)-1)
        while(aux4 == aux3):
            aux4 = random.randint(0, len(child)-1)
        
        child[aux3] , child[aux4] = child[aux4] , child[aux3]

    return child


population = populationGenerate(50)
parents = selectTwoRoutes(population)
bestYet = parents[0]
for i in range(100):
    for j in range(50):
        child = crossover(parents)
        print(child)
        population.append(child)
    parents = selectTwoRoutes(population)
    bestYet = parents[0]
    print(bestYet)


print("\nthe best route chosen was:\n")
print(bestYet)
