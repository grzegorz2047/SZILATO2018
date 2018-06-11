from random import *
from math import floor
from map import *

#Klasa dla pojedynczego gatunku
class Phenotype:
    def __init__(self, genotype, tileMap):
        self.tileMap = tileMap
        self.genotype = genotype
        
    
    def initRandomGenes(self):
        self.genotype.initRandomGenes()
        
    def getGeneAt(self, index):
        return self.genotype.getGeneAt(index)
    
    def getFitness(self):
        #print("fitness ", self.genotype.calculateFitness()) 
        return self.genotype.calculateFitness()
    
    def crossover(self, partner):
        gensLength = len(self.genotype.monsterGenes)
        childGenes = []
        midpoint = floor(randrange(gensLength)); 
        
        for i in range(0, gensLength-1):
            if i > midpoint:
                childGenes.append(self.getGeneAt(i))
            else:
                childGenes.append(partner.getGeneAt(i))
        childGenotype = Genotype(self.tileMap)
        childGenotype.initGenes(childGenes)
        child = Phenotype(childGenotype, self.tileMap)
        return child

    def mutate(self, ):
        if random.uniform(0, 1) <= 0.01:
            return randrange()
        
    def initPhenotype(self):
        self.genotype = Genotype()
        
class Genotype:
    monsterGenes = []
    def __init__(self, tileMap):
        self.tileMap = tileMap
    
    def initGenes(self, genes):
        self.monsterGenes = genes
        
    def initRandomGenes(self):
        stats = [#hp, attack, defense, type
            [50, 60, 20, 0],
            [100, 80, 30, 1],
            [175, 110, 40, 2],
            [275, 150, 50, 3],
            [400, 200, 60, 4],
            [650, 260, 70, 5]
        ]
        genNum = 10
        while genNum > 0:
            randX = randrange(10)
            randY = randrange(10)
            randIndex = randrange(6)
            monsterGot = stats[randIndex]
            geneObj = GeneMonster(randX, randY, monsterGot[0], monsterGot[1], monsterGot[2], monsterGot[3])
            self.monsterGenes.append(geneObj)
            genNum = genNum - 1
    def getGeneAt(self, index):
        return self.monsterGenes[index]
    
    def calculateFitness(self):#gracz ma 700 hp na poczatku, zeby mial szanse na starcie
        playerHp = 700
        playerAt = 70
        playerDeff = 20
        
        fitnesSum = 0
        monsterAllStrength = 0
        monsterAllDef = 0
        monsterAllHp = 0        
        mapWidth = 10
        #print(self.tileMap)
        for gene in self.monsterGenes:
        
            mapTileType = self.tileMap[gene.y][gene.x];
            #print("type ", mapTileType)
            grass = "."
            if mapTileType == grass:
                #print("gut")
                fitnesSum = fitnesSum + 50
            else:
                fitnesSum = fitnesSum - 1000
            monsterAllStrength = monsterAllStrength + gene.at
            monsterAllDef = monsterAllDef + gene.deff
            monsterAllHp = monsterAllHp + gene.hp
        fitnesSum = fitnesSum - abs(playerHp - monsterAllHp)
        fitnesSum = fitnesSum - (abs(playerAt - monsterAllStrength) *2)
        fitnesSum = fitnesSum - (abs(playerDeff - monsterAllDef))
        return fitnesSum
        
class GeneticAlgorithmImplementation:
    population = []
    populationSize = 50
    generationNumber = 0
    
    def run(self, tileMap):
        self.tileMap = tileMap
        self.createFirstPopulation()
        self.evolvePopulation()
        
    def evolvePopulation(self):
        while self.generationNumber < 150:
            self.generationNumber = self.generationNumber + 1
            self.combineBestSpecies()
            print ("Best fitness for ", self.generationNumber, " generation is ", self.getBestFitnessValue())

    def createFirstPopulation(self):
        for x in range(0, self.populationSize):
            pheno = Phenotype(Genotype(self.tileMap), self.tileMap)
            pheno.initRandomGenes()
            self.population.append(pheno)
    def getBestFitnessValue(self):
        max = -sys.maxsize -1
        for one in self.population:
            currentFitness = one.getFitness()
            if currentFitness > max:
                max = currentFitness
        return max
        
    def getBestUnitFromWheel(self, units):
        #print("unit size ", len(units))
        max = units[0]
        for one in units:
            currentFitness = one.getFitness()
            if currentFitness > max.getFitness():
                max = one
        return max
        
    def combineBestSpecies(self):
        species = []
        numOfSpeciesToBorn = self.populationSize
        newPopulation = []
        for one in self.population:
            species.append(one)
        
        while len(species) > 0:
            #print("species len ", len(newPopulation))
            
            bestOne = self.getBestUnitFromWheel(species)
            species.remove(bestOne)
            if len(species) == 0:
                bestTwo = newPopulation[0]
            else: 
                bestTwo = self.getBestUnitFromWheel(species)
            newChild = bestOne.crossover(bestTwo)
            newPopulation.append(newChild)
        self.population = newPopulation
class GeneMonster:
    def __init__(self, x, y, hp, at, deff, type):
        self.x = x
        self.y = y
        self.hp = hp
        self.at = at
        self.deff = deff
        self.type = type