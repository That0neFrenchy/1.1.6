import random
import math
import pygame
import time


from dataclasses import dataclass


@dataclass
class Ball:
    ball_max_speed:float
    ball_x:float
    ball_y:float
    ball_speed_x:float
    ball_speed_y:float


    def step(self):
        # Detect collision between ball and right wall  
        if self.ball_x + self.ball_speed_x > 690:
            self.ball_speed_x = random.random() * -2 - self.ball_speed_x
        # Detect collision between ball and left wall
        if self.ball_x - self.ball_speed_x < 110:
            self.ball_speed_x = random.random() * 2 + self.ball_speed_x
        # Detect collisions with bottom wall
        if self.ball_y + self.ball_speed_y > 490:
            self.ball_speed_y = random.random() * -2 - self.ball_speed_y
        #Detect collisions with top wall
        if self.ball_y - self.ball_speed_y < 110:
            self.ball_speed_y = random.random() * 2 + self.ball_speed_y
        # Starting movement of ball
        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y
        if self.ball_speed_x < -self.ball_max_speed:
            self.ball_speed_x = -self.ball_max_speed
        if self.ball_speed_y < -self.ball_max_speed:
            self.ball_speed_y = -self.ball_max_speed
        if self.ball_speed_x > self.ball_max_speed:
            self.ball_speed_x = self.ball_max_speed
        if self.ball_speed_y > self.ball_max_speed:
            self.ball_speed_y = self.ball_max_speed
       


    def reverse(self):
        self.ball_speed_x = self.ball_speed_x * -1
        self.ball_speed_y = self.ball_speed_y * -1




pygame.init()







display_width = 800
display_height = 600




display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dodgeball')




black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)
brown = (160,82,45)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)




clock = pygame.time.Clock()
crashed = False




player_x = 200
player_y = 300
player_speed = 3
player_color = brown




clock_value = 0




kill_ball = Ball(7.5, 400, 150, 2, 2)
kill_orb = Ball(7.5, 400, 300, 0, 0)
block_time = -1
block_duration = 30




move_player_left = False
move_player_right = False
move_player_up = False
move_player_down = False




# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)
 
def distance (x1, y1, x2, y2):
    """
    compute the distance between two points
    """
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)




while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                move_player_right = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move_player_left = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                move_player_up = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move_player_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                move_player_right = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                move_player_left = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                move_player_up = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                move_player_down = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                block_time = clock_value


    if move_player_right and player_x < 708:
        player_x += player_speed
    if move_player_left and player_x > 92:
        player_x -= player_speed
    if move_player_up and player_y > 92:
        player_y -= player_speed
    if move_player_down and player_y < 508:
        player_y += player_speed


    #start kill orb movement aftter 10 sec
    if clock_value == 600:
        kill_orb.ball_speed_y = kill_ball.ball_speed_y
        kill_orb.ball_speed_x = kill_ball.ball_speed_x
    kill_ball.step()
    kill_orb.step()
   
    text = font.render(f"good luck {clock_value // 60}", True, green, blue)
    clock_value += 1




    #start display
    display.fill(black)
    pygame.draw.rect(display, yellow, pygame.Rect(50, 50, 700, 500))
    pygame.draw.rect(display, white, pygame.Rect(70, 70, 660, 460))


    if block_time + block_duration > clock_value:
        player_color = blue
    else:
        player_color = brown




    pygame.draw.circle(display,player_color, (player_x,player_y), 22) #player
    pygame.draw.circle(display, red, (kill_ball.ball_x,kill_ball.ball_y), 40) #Kill ball
    pygame.draw.circle(display, red, (kill_orb.ball_x,kill_orb.ball_y), 40)






    display.blit(text, (360,20))




    pygame.display.update()
    clock.tick(60)
    if distance (player_x, player_y, kill_ball.ball_x, kill_ball.ball_y) < 62:
        if block_time + block_duration < clock_value:
            time.sleep(2)
            crashed = True
        else:
            kill_ball.reverse()
    if distance (player_x, player_y, kill_orb.ball_x, kill_orb.ball_y) < 62:
        if block_time + block_duration < clock_value:
            time.sleep(2)
            crashed = True
        else:
            kill_orb.reverse()
    if distance (kill_ball.ball_x, kill_ball.ball_y, kill_orb.ball_x, kill_orb.ball_y) < 62:
        # both kill balls bounce of one another
        kill_ball.reverse()
        kill_orb.reverse()
       


pygame.quit()
quit()









