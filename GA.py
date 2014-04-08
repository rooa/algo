from math import sqrt
from random import random, shuffle
from copy import copy

#N = 20                                    # Number of genes holding
L = 50                                  # Length of a gene
GENERATION = 15000

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distance(self, op):
        return sqrt((self.x - op.x)**2 + (self.y - op.y)**2)
   
points = [Point(random(),random()) for i in range(L)]

class Gene():
    def __init__(self):
        self.gene = []                    # gene computed from permutaion
        self.length = L

        index = range(L)
        shuffle(index)
        self.permutation = index
        self.initGene()

    def initGene(self):
        start = range(L)
        for i in self.permutation:
            self.gene.append(start.index(i))
            start.remove(i)

def path_score(gene):
    res = 0
    tmp = range(L)
    first = tmp[gene[0]]

    prev = tmp[gene[0]]
    tmp.remove(prev)
    for i in range(1,L):
        p = tmp[gene[i]]
        #print p
        res += points[prev].distance(points[p])
        tmp.remove(p)
        prev = p

    res += points[prev].distance(points[first])
    return res

def cityToGene(city):
    result = []
    start = range(L)
    for i in city:
        result.append(start.index(i))
        start.remove(i)
    return result

def geneToCity(gene):
    result = []
    tmp = range(L)
    for i in range(L):
        p = tmp[gene[i]]
        result.append(p)
        tmp.remove(p)
    return result

class GeneticAlgorithm():
    def __init__(self,N):
        self.population = N
        self.genes = [Gene().gene for i in range(N)]
        #print self.genes
        self.scores = {}
        self.updateScores()
        
    def updateScores(self):
        self.scores = {}
        for i in range(len(self.genes)):
            self.scores[path_score(self.genes[i])] = self.genes[i]

    def crossOver(self,div):
        parents = {}
        temp = self.scores.copy()
        for i in range(self.population/2):
            min_ = min(temp.keys())
            parents[min_] = temp[min_]
            del(temp[min_])
        l = len(parents)
        children = []
        parent_genes = parents.values()
        for i in range(l):
            for j in range(i+1,l):
                new = parent_genes[i][:div] + parent_genes[j][div:]
                if not new in children:
                    children.append(new)
                if len(children) > self.population/2:
                    break
            if len(children) > self.population/2:
                break
            

        self.genes = self.genes + children
        #print children
        self.updateScores()


    def crossOver(self,div):
        parents = {}
        temp = self.scores.copy()
        for i in range(self.population/2):
            min_ = min(temp.keys())
            parents[min_] = temp[min_]
            del(temp[min_])
        l = len(parents)
        children = []
        parent_genes = parents.values()
        for i in range(l):
            for j in range(i+1,l):
                new1 = parent_genes[i][:div] + parent_genes[j][div:]
                new2 = parent_genes[j][:div] + parent_genes[i][div:]
                if not new1 in children:
                    children.append(new1)
                if not new2 in children:
                    children.append(new2)
                if len(children) > self.population/2:
                    break
            if len(children) > self.population/2:
                break
            

        self.genes = self.genes + children
        #print children
        self.updateScores()
            
        
        
    def crossOver_order(self,div):
        parents = {}
        temp = self.scores.copy()
        for i in range(self.population/2):
            min_ = min(temp.keys())
            parents[min_] = temp[min_]
            del(temp[min_])
            if len(temp.keys()) == 0:
                break
        l = len(parents)
        children = []
        parent_genes = parents.values()
        for i in range(l):
            pg1 = parent_genes[i]
            for j in range(i+1,l):
                pg2 = parent_genes[j]
                g1 = geneToCity(pg1)
                g1temp = geneToCity(pg1)
                g2 = geneToCity(pg2)
                g2temp = geneToCity(pg2)

                for i in range(div):
                    g2temp.remove(g1[:div][i])
                    g1temp.remove(g2[:div][i])
                g1 = g1[:div] + g2temp
                g2 = g2[:div] + g1temp
                
                g1 = cityToGene(g1)
                g2 = cityToGene(g2)
                if not g1 in children:
                    children.append(g1)
                if not g2 in children:
                    children.append(g2)
                if len(children) > self.population/2:
                    break
            if len(children) > self.population/2:
                break
            

        self.genes = self.genes + children
        #print children
        self.updateScores()

        
    def selection(self):
        selected = []
        temp = self.scores.copy()
        Pop = self.population
        while len(selected) < Pop:
            min_ = min(temp.keys())
            selected.append(temp[min_])
            del(temp[min_])
        self.genes = selected
        self.updateScores()

        
                    
    def mutation_switch(self,p):
        if p < 0.1:
            pass
            
    def mutation_reverse(self):
        #import ipdb; ipdb.set_trace();
        for i in range(5):
            G = len(self.genes)
            r = random()
            idx1 = int(r*100) % G
            g = self.genes[idx1]
            l = len(g)
            p1 = int(r*100) % l
            p2 = int(random()*100) % l
            tmp = geneToCity(g)
            if p1 < p2:
                tmp[p1:p2] = list(reversed(tmp[p1:p2]))
            else:
                tmp[p2:p1] = list(reversed(tmp[p2:p1]))
            #tmp = list(reversed(tmp))
            self.genes[idx1] = cityToGene(tmp)

        self.updateScores()
        print "mutated"


    def mutation_tenza(self):
        #import ipdb; ipdb.set_trace();
        for i in range(5):
            G = len(self.genes)
            r = random()
            idx1 = int(r*100) % G
            g = self.genes[idx1]
            tmp = geneToCity(g)
            l = len(g)
            p1 = int(r*100) % l
            p2 = int(random()*100) % l
            p3 = int(random()*100) % l
            while p3 != max([p1,p2,p3]):
                p3 = int(random()*100) % l
            if p1 < p2 :
                piece = tmp[p1:p2]
                tmp = tmp[:p1] + tmp[p2:p3] + piece + tmp[p3:]
            else:
                piece = tmp[p2:p1]
                tmp = tmp[:p2] + tmp[p1:p3] + piece + tmp[p3:]
            #tmp = list(reversed(tmp))
            self.genes[idx1] = cityToGene(tmp)

        self.updateScores()
        print "mutated"

        
    def bestScore(self):
        min_ = min(self.scores.keys())
        return min_


def visualize(points_, path):
    from matplotlib import pyplot
    print len(path)
    print len(points)
    # plot points
    for i in range(len(path)):
        p1,p2 = path[i-1],path[i]
        pyplot.plot([points_[p1].x,points_[p2].x],[points_[p1].y,points_[p2].y],"b-")


    #pyplot.axis([0,1,0,1])    
    pyplot.show()


    

def solve():
    solver = GeneticAlgorithm(200)
    counter = 0
    import ipdb
    b = solver.bestScore()
    while counter < GENERATION:
        #ipdb.set_trace()
        if counter % 10 == 0:
            print counter,":", solver.bestScore()
        p = random()
        solver.crossOver_order(int(100*p)%10 + 10)
        if p < 0.2:
            if p < 0.1:
                solver.mutation_tenza()
            else:
                solver.mutation_reverse()
        solver.selection()
        counter += 1
    print b ,"->", solver.bestScore()

    print
    
    for i in range(len(points)):
        print points[i].x, points[i].y

    print

    for i in geneToCity(solver.scores[solver.bestScore()]):
        print i, "->",
        
    print

    visualize(points, geneToCity(solver.scores[solver.bestScore()]))
    
