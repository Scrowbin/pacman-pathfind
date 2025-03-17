import pygame


TITLE = 'Pac-Man'
file="map.txt"

# WORLD_SIZE = 28
BLOCK_SIZE = 32


assets = {
                        '%': pygame.image.load('graphic_assets/wall.png'),
                        'O': pygame.image.load('graphic_assets/power.png'),
                        '.': pygame.image.load('graphic_assets/feast.png'),
                        'P': pygame.image.load('graphic_assets/pac.png'),
                                      }
wallTextures = {
     'horizontal': pygame.image.load('graphic_assets/wall.png'),
     'vertical' : pygame.image.load('graphic_assets/wall2.png'),
}
map = []

with open(file) as f:
            for line in f:
                row = []
                for block in line:
                    row.append(block)
                map.append(row)


WIDTH = len(map[0])*BLOCK_SIZE
HEIGHT =len(map)*BLOCK_SIZE
# dynamically assigning resolution
pygame.init()
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
# def getTexture(col, row):
#     # for columns
#     if col > 0 and col < len(map[row]) - 1 and map[row][col - 1] == '%' and map[row][col + 1] == '%':
#         return wallTextures['vertical']
#     if row > 0 and row < len(map) - 1 and map[row - 1][col] == '%' and map[row + 1][col] == '%':
#         return wallTextures['horizontal']
         
def draw():
        
        for y, row in enumerate(map):
            for x, block in enumerate(row):
                image = assets.get(block, None)
                # texture = getTexture(x, y)
                if image:
                    # scale
                    # scaledTextures = pygame.transform.scale(assets[block], (BLOCK_SIZE, BLOCK_SIZE))
                    # blitzkrieg
                    screen.blit(assets[block], (x*BLOCK_SIZE, y*BLOCK_SIZE))
                # if texture:
                #     # scaledTextures = pygame.transform.scale(texture, (BLOCK_SIZE, BLOCK_SIZE))
                #     screen.blit(texture, (x*BLOCK_SIZE, y*BLOCK_SIZE))



playing = True
while playing:
    screen.fill((0,0,0))
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    pygame.display.flip()
    