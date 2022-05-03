
import pygame, sys, random

from pygame.locals import *

screen_width = 600
screen_height = 600

grid_size = 20

grid_width = screen_width/grid_size
grid_height = screen_height/grid_size

light_green = (0,170,140)
dark_green = (0,140,120)
food_color = (250,200,0)
snake_color = (34,34,34)

up = (0,-1)
down = (0,1)
right = (1,0)
left = (-1,0)

class Snake():
    
    def __init__(self):

        self.positions = [(screen_width/2,screen_height/2)]
        self.length = 1
        self.direction = right
        self.color = snake_color
        self.score = 0

    def draw(self,surface):

        for p in self.positions:

            snake = pygame.Rect((p[0],p[1]),(grid_size,grid_size))
            pygame.draw.rect(surface,self.color,snake)

    
    def act(self):
        now = self.positions[0]
        x,y = self.direction
        new = ((now[0] + x*grid_size),(now[1] + y*grid_size))


        if new[0] in range(0,screen_width) and new[1] in range(0,screen_height) and not new in self.positions[2:]:
            self.positions.insert(0,new)
            if len(self.positions) > self.length :
                self.positions.pop()

        else:
            self.reset()


    def reset(self):
        self.length = 1
        self.positions = [(screen_width/2,screen_height/2)]
        self.direction = right
        self.score = 0


    def handle_keys(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
        
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    self.turn(up)

                elif event.key == pygame.K_DOWN:
                    self.turn(down)

                elif event.key == pygame.K_RIGHT:
                    self.turn(right)

                elif event.key == pygame.K_LEFT:
                    self.turn(left)
    def turn(self,direction):

        if(direction[0] * -1, direction[1] * -1) == self.direction:
            return

        else:
            self.direction = direction


class Food():

    def __init__(self):

        self.position = (0,0)
        self.color = food_color
        self.randpos()

    def randpos(self):

        self.position = (random.randint(0, int(grid_width-1))*grid_size,random.randint(0, int(grid_height-1))*grid_size)

    
    def draw(self,surface):
        yemek = pygame.Rect((self.position[0], self.position[1]), (grid_size, grid_size))
        pygame.draw.rect(surface, self.color, yemek)


def draw_Grid(surface):

    for y in range(0,int(grid_height)):
        for x in range(0,int(grid_width)):

            if((x+y) % 2) == 0 : 

                kare = pygame.Rect((x*grid_size, y*grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, light_green, kare)

            else:
                kare2 = pygame.Rect((x*grid_size, y*grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, dark_green, kare2)

def main():

    pygame.init() # bununla beraber projemiz başlamış oluyor.

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Yılan Oyunu")

    font = pygame.font.SysFont("arial", 20)

    surface = pygame.Surface(screen.get_size())
    surface.convert()
    
    snake = Snake()
    food = Food()

    while True:
        clock.tick(10)
        snake.handle_keys()
        snake.act()
        draw_Grid(surface)

        if(snake.positions[0] == food.position):
            snake.length += 1
            snake.score += 1
            food.randpos()

        

        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))

        score_metni = font.render(f"Score :{snake.score}",True,(0,0,0))
        screen.blit(score_metni, (10,10))

        pygame.display.update() 
 
main()




