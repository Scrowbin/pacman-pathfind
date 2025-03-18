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


kaizen = visualization()
kaizen.play()

