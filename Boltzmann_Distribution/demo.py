import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
import sklearn

# default settings

NUM_PERSON = 1000
ITER = 60
MONEY = 20

class person():
    def __init__ (self, idx, money):
        self.id = idx
        self.pocket = money
        self.avail = True
    
class exchange():
    def __init__ (self):
        self.table = []            # maybe is not nessasary
        self.pairs = []
        self.alive = []
    
    def initialization (self):
        for i in range(NUM_PERSON):
            self.table.append(person(i, MONEY))
        self.pairs = list(range(0, NUM_PERSON))
        self.alive = list(range(0, NUM_PERSON))

    def pairing (self):
        random.shuffle(self.pairs)
        print(self.pairs)

    def doexchange (self):
        for idx, p1 in enumerate(self.pairs):
           print ("idx: {}, p1: {}, p2: {}".format(idx, p1, self.pairs[len(self.alive) - idx - 1]))
           if random.random() < 0.5:
               self.table[p1].pocket += 1
               self.table[self.pairs[len(self.alive) - idx - 1]].pocket -= 1
           else: 
               self.table[p1].pocket -= 1
               self.table[self.pairs[len(self.alive) - idx - 1]].pocket += 1

           if self.table[idx].pocket <= 0:
               self.table[idx].avail = False

           if self.table[self.pairs[len(self.alive) - idx - 1]].pocket <= 0:
               self.table[idx].avail = False 

           if idx >= int(len(self.pairs)/2 - 1):
               break
    
    def printtable(self):
        for t in self.table:
            print("ID:", t.id, "MONEY:", t.pocket)
    
    def go(self):
        for i in range(ITER):
            self.pairing()
            self.doexchange()
            self.printtable()
    
       
    
        




# main

game = exchange()
game.initialization()
game.go()

SUM = 0
SUM_LIST = []
print("=="*5, "result", "=="*5)
for i in range(NUM_PERSON):
    print (game.table[i].id, game.table[i].pocket)
    SUM += game.table[i].pocket
    SUM_LIST.append(game.table[i].pocket)

print("SUM:", SUM)    
plt.hist(SUM_LIST)
plt.show()
