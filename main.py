import os
import heapq

class main:
    def __init__(self, file='map.txt'):
        self.map = []
        self.file= file
        with open(file) as f:
            for line in f:
                row = []
                for block in line:
                    row.append(block)
                self.map.append(row)
    def getAL(self):
        pacLoc = []
        # just in case these two needs to be seperated
        foodLoc = []
        powerUpLoc = []
        for y, row in enumerate(self.map):
            for x, col in enumerate(row):
                if col == 'P':
                    pacLoc.append((x, y))
                if col == '.':
                    foodLoc.append((x,y))
                if col == 'O':
                    powerUpLoc.append((x,y))
        itemsLoc = foodLoc + powerUpLoc # extending values

        D = []
        # distance from pacman to itemsLoc
        pac_x, pac_y = pacLoc[0]
        i = 1 # assigning them "names"
        for item in itemsLoc:
            x, y = item
            manhattan_distance = abs(pac_x - x) + abs(pac_y - y)
            heapq.heappush(D, (manhattan_distance, (i, manhattan_distance)))
            i+=1
        # generates all le path
        for state, __ in D:
            # nhet vao mot cai dict() 



