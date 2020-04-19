import cv2
import numpy as np
from matplotlib import pyplot as plt
import random
import sklearn

# default settings

NUM_PERSON = 1000
ITER = 30
MONEY = 4

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
        #print(self.pairs)

    def doexchange (self):
        for idx, p1 in enumerate(self.pairs):
           p2 = self.pairs[len(self.alive) - idx - 1]
           #print ("idx: {}, p1: {}, p2: {}".format(idx, p1, self.pairs[len(self.alive) - idx - 1]))
           if random.random() <= 0.5:  # p1 win and p2 lose
               if self.table[p2].pocket > 0: 
                   self.table[p1].pocket += 1
                   self.table[p2].pocket -= 1
           else:  # p2 win and p1 lose
               if self.table[p1].pocket > 0:
                   self.table[p1].pocket -= 1
                   self.table[p2].pocket += 1

           if idx >= int(len(self.pairs)/2 - 1):
               break
    
    def printtable(self):
        for t in self.table:
            print("ID:", t.id, "MONEY:", t.pocket)
    
    def go(self):
        for i in range(ITER):
            self.pairing()
            self.doexchange()
#            self.printtable()
    

game = exchange()
game.initialization()
game.go()

### evaluation ###

SUM = 0
SUM_LIST = []
PRICE = list(range(0, NUM_PERSON))
PRICE_TABLE = [0] * NUM_PERSON

print("=="*5, "result", "=="*5)
for i in range(NUM_PERSON):
    print (game.table[i].id, game.table[i].pocket)
    SUM += game.table[i].pocket
    SUM_LIST.append(game.table[i].pocket)
    
    PRICE_TABLE[game.table[i].pocket] += 1 

DELETE = []
NEW_PRICE_TABLE = []
NEW_PRICE = []

for i, p in enumerate(PRICE_TABLE):
    if p == 0:
        DELETE.append(i)

for p in range(len(PRICE_TABLE)):
    if p not in DELETE:
        NEW_PRICE_TABLE.append(PRICE_TABLE[p])
        NEW_PRICE.append(PRICE[p])
        


plt.scatter(NEW_PRICE, NEW_PRICE_TABLE)
plt.show()
