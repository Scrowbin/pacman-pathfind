import os
import heapq

class main:
    def __init__(self, file='map.txt'):
        self.map = []
        self.file= file
        self.pacLoc = []
        self.foodLoc = []
        self.powerUpLoc = []
        self.actions = []
        with open(file) as f:
            for line in f:
                row = []
                for block in line:
                    row.append(block)
                self.map.append(row)
        self.getPos()

    def getPos(self):
        for x, row in enumerate(self.map):
            for y, col in enumerate(row):
                if col == 'P':
                    self.pacLoc.append((x, y))
                if col == '.':
                    self.foodLoc.append((x,y))
                if col == 'O':
                    self.powerUpLoc.append((x,y))
    def h(self, pos):
        pac_x, pac_y = self.pacLoc[0]
        x, y = pos
        return abs(pac_x - x) + abs(pac_y - y)
    # assign names and shit
    # def AL(self):
        
    def go(self, action , state):
        pac_x, pac_y = state.pacLoc[0]
        if pac_x >= 0 and pac_x < len(self.map[0]) and pac_y >=0 and pac_y < len(self.map):
            state.pacLoc.pop(0)
            if action == 'L':
                pac_x -= 1
                state.pacLoc.append((pac_x, pac_y))
                state.actions.append('West')
            if action == 'R':
                pac_x += 1
                state.pacLoc.append((pac_x, pac_y))
                state.actions.append('East')
            if action == 'U':
                pac_y += 1
                state.pacLoc.append((pac_x, pac_y))
                state.actions.append('North')
            if action == 'D':
                pac_y -=1
                state.pacLoc.append((pac_x, pac_y))
                state.actions.append('South')

        return state
    def expand(self, state):
        moves = ['L', 'R', 'U', 'D']
        for m in moves:
            state.go(m, state)
        

    def AStarAlgo(self):
        movementSet = ['North', 'East', 'West', 'South', 'Stop']
        expanded = []
        path = []
        frontier = []
        # heapq.heappush()
       


