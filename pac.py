import pygame

class visualization:
    BLOCK_SIZE = 32
    TITLE = 'Pac-Man'
    assets = {
            '%': pygame.image.load('graphic_assets/wall.png'),
            'O': pygame.image.load('graphic_assets/power.png'),
            '.': pygame.image.load('graphic_assets/feast.png'),
            'P': pygame.image.load('graphic_assets/pac.png'),}
        
    
    def __init__(self, map = []):
        
        self.map = map
        
        WIDTH = len(self.map[0])*self.BLOCK_SIZE
        HEIGHT =len(self.map)*self.BLOCK_SIZE
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    
    def draw(self, map = []):
        if (map== []):
            map = self.map
        for y, row in enumerate(map):
            for x, block in enumerate(row):
                image = self.assets.get(block, None)
                if image:
                    self.screen.blit(self.assets[block], (x*self.BLOCK_SIZE, y*self.BLOCK_SIZE))


    def play(self):
        pygame.init()   
        pygame.display.set_caption(self.TITLE)
        playing = True
        while playing:
            self.screen.fill((0,0,0))
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
            pygame.display.flip()

    #needs the map without anything as a base lol 
    def getMapFromState(self,state):
        localMap = self.map
        for i,locs in enumerate(state):
            for location in locs:
                x,y = location
                if (i==0):
                    localMap[x][y] = "P"
                elif i==1:
                    localMap[x][y] = "."
                elif i==2:
                    localMap[x][y] = "O"
        return localMap
                    

        
# này sẽ get map without anything
def getMapFromFile(file='map.txt'):
        map = []
        file= file
        with open(file) as f:
            for line in f:
                row = []
                for block in line:
                    if (block == "%"):
                        row.append(block)
                    else:
                        row.append(" ")
                map.append(row)
        return map


kaizen = visualization(getMapFromFile())
kaizen.draw(kaizen.getMapFromState([[(1,3)],[(2,2),(17,7),(9,2)],[(15,12),(10,10),(3,3)]]))
kaizen.play()

