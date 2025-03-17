import pygame

class visualization:
    BLOCK_SIZE = 32
    TITLE = 'Pac-Man'
    assets = {
            '%': pygame.image.load('graphic_assets/wall.png'),
            'O': pygame.image.load('graphic_assets/power.png'),
            '.': pygame.image.load('graphic_assets/feast.png'),
            'P': pygame.image.load('graphic_assets/pac.png'),}
        
    
    def __init__(self, file='map.txt'):
        self.file= file
        self.map = []
        with open(file) as f:
                    for line in f:
                        row = []
                        for block in line:
                            row.append(block)
                        self.map.append(row)
        WIDTH = len(self.map[0])*self.BLOCK_SIZE
        HEIGHT =len(self.map)*self.BLOCK_SIZE
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    def draw(self):
        
        for y, row in enumerate(self.map):
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
            


# WORLD_SIZE = 28


kaizen = visualization()
kaizen.play()
# wallTextures = {
#      'horizontal': pygame.image.load('graphic_assets/wall.png'),
#      'vertical' : pygame.image.load('graphic_assets/wall2.png'),
# }



# dynamically assigning resolution


# 

