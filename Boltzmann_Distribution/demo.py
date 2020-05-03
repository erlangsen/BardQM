import cv2
import numpy as np, scipy as sp
from matplotlib import pyplot as plt
import random
import sklearn

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
        self.money = 0
        self.num_person = 0
    
    def initialization (self, money, num_person):
        self.money = money
        self.num_person = num_person

        for i in range(self.num_person):
            self.table.append(person(i, self.money))
        self.pairs = list(range(0, self.num_person))
        self.alive = list(range(0, self.num_person))

    def pairing (self):
        random.shuffle(self.pairs)

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
            print("ID:", t.id, "money:", t.pocket)

    def showboard(self):        
        price_table = [0] * self.num_person
        price = list(range(0, self.num_person))
        for i in range(self.num_person):
            print(self.table[i].id, self.table[i].pocket)
            price_table[self.table[i].pocket] += 1

        new_price_table = [price_table[i] for i in range(len(price_table)) if (price_table[i] != 0)]  
        new_price = [price[i] for i in range(len(price_table)) if (price_table[i] != 0)] 

        x = np.arange(0, new_price[-1], 0.1)
        y = np.exp(-x / self.money) / 4

        plt.plot(x,y, color = "red")
        plt.scatter(new_price, list(np.array(new_price_table)/self.num_person))
        plt.show()

    def play(self, times):
        for i in range(times):
            self.pairing()
            self.doexchange()
#            self.printtable()
    


if __name__ == "__main__" :
    game = exchange()
    game.initialization(money = 4, num_person = 1000)  # 1000 person with 4 dollars each.
    game.play(times = 100)                             # exchange 100 times.
    game.showboard()
