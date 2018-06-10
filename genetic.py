from random import *
from math import floor
from map import *

#Klasa dla pojedynczego gatunku
class Phenotype:
    fitness = 0
    genotype = None
    def __init__(self, tileMap):
        self.tileMap = tileMap
    
    def getGeneAt(self, index):
        return genotype.getGeneAt(index)
    
    def getFitness(self):
        
    def crossover(self, partner):
        gensLength = len(self.genotype)
        childGenes = []
        midpoint = floor(randrange(gensLength)); 
        
        for i in range(0, gensLength-1):
            if i > midpoint:
                childGenes.append(self.getGeneAt(i))
            else:
                childGenes.append(partner.getGeneAt(i))
        childGenotype = Genotype(childGenes)
        child = Phenotype(childGenotype, tileMap)
        return child

    def mutate(self):
        mutationRate = 0.01
        
    def initPhenotype(self):
        self.genotype = Genotype()
        
class Genotype:
    monsterTilesGenes = []
    
    def getGeneAt(self, index):
        return self.monsterTilesGenes[index]
    
    def calculateFitness(self):
            

class GeneticAlgorithmImplementation:
    population = []
    populationSize = 50
    generationNumber = 0
    
    def run(self, tileMap):
        self.createFirstPopulation(tileMap)
        self.evolvePopulation()
    def evolvePopulation():
        while generationNumber < 100:
            generationNumber = generationNumber + 1
            self.combineBestSpecies()
            print ("Best fitness for ", self.generationNumber, " generation is ", self.getBestFitnessValue())

    def createFirstPopulation(self, tileMap):
        for x in range(0, populationSize-1):
            population.append(Phenotype(tileMap))
    def getBestFitnessValue():
        max = -sys.maxsize -1
        for one in population:
            currentFitness = one.getFitness()
            if currentFitness > max:
                max = currentFitness
        return max
    def getBestUnitFromWheel(units):
        max = -sys.maxsize -1
        for one in population:
            currentFitness = one.getFitness()
            if currentFitness > max:
                max = currentFitness
        return max
    def combineBestSpecies(self):
        for one in population:
            currentFitness = one.getFitness()
            if currentFitness > max:
                max = currentFitness
class Monster:
     