import random


def roulet(npopulation,nPais):
    fitnessAbs=[]
    fitnessRelative=[]
    chosenParents=[]
    roulet=[]
    aux=0 
    for i in range(len(npopulation)):
        fitness=calcFitness(npopulation[i])
        fitnessAbs.append(fitness)
        aux+=fitness

    roulet.append(0)
    for i in range(len(npopulation)):
        fitnessRelative.append(fitnessAbs[i]/aux)
        roulet.append(round(roulet[i]+fitnessRelative[i],3))
        
    for a in range(nPais):
        numero=random.randint(0,int(roulet[len(roulet)-1]*1000))
        for i in range(len(roulet)-1):
            if(numero>roulet[i]*1000 and numero<=roulet[i+1]*1000):
                chosenParents.append(npopulation[i])
    return chosenParents

class city1:
    ind = 0
    city = 1
    dist = [0, 2, 999, 3, 6]

class city2:
    ind = 1
    city = 2
    dist = [2, 0, 4, 3, 999]

class city3:
    ind = 2
    city = 3
    dist = [999, 4, 0, 7, 3]

class city4:
    ind = 3
    city = 4
    dist = [3, 3, 7, 0, 3]

class city5:
    ind = 4
    city = 5
    dist = [6, 999, 3, 3, 0]

# Fitness is multiplied by -1 because it makes the
# smallest path the biggest score
def calcFitness(dna):
    fitness = 0
    for i in range (1, len(dna)):
        fitness += dna[i].dist[dna[i-1].ind]

    return (1/fitness)

def calcDist(dna):
    distance = 0
    for i in range (1, len(dna)):
        distance += dna[i].dist[dna[i-1].ind]
    
    return distance


def bestOfPop(population):
    bestInPop = 999999
    for i in range(len(population)):
        if(calcDist(population[i]) < bestInPop):
            bestRoute = population[i]
    return bestRoute


def dnaGenerate():
    dna = [city1, city2, city3, city4, city5]
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

def crossoverlite(parents):
    aux1 = 0
    aux2 = 0
    child = parents[1]
    #printRoute(child)
    while(aux1 < 5):
        if(aux2==1 or aux2==2):
            aux2 += 1
            continue
        if(parents[0][aux1] in child):
            aux1 += 1    
            continue

        child[aux2] = parents[0][aux1]
        aux2 += 1
        aux1 += 1
    
    if((random.randint(0,10000) < 3)):
        aux3 = random.randint(0, len(child)-1)
        aux4 = random.randint(0, len(child)-1)
        while(aux4 == aux3):
            aux4 = random.randint(0, len(child)-1)
        
        child[aux3] , child[aux4] = child[aux4] , child[aux3]

    return child


def printRoute(route):
    print("{0} -- {1} -- {2} -- {3} -- {4}".format(route[0].city, route[1].city, route[2].city, route[3].city, route[4].city))
    print("route score: {}".format(calcDist(bestYet)))

def printParent(parents):
    print("{0} -- {1} -- {2} -- {3} -- {4}".format(parents[0].city, parents[1].city, parents[2].city, parents[3].city, parents[4].city))



genSize = 10
numberOfGens = 6
population = populationGenerate(genSize)
parents = roulet(population, 2)
bestYet = bestOfPop(population)
for i in range(numberOfGens-1):
    population.append(bestYet)
    
    for j in range(genSize):
        child = crossoverlite(parents)
        population.append(child)
    
    for x in population:
        printRoute(x)

    parents = roulet(population, 2)
    bestYet = bestOfPop(population)


print("\nThe best route chosen was:\n")
printRoute(bestYet)




