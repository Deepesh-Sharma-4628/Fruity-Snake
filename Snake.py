import pygame
import random
import os

pygame.mixer.init()

pygame.init()



# Colors
white = (255, 255, 255)
red = (255, 4, 29)
black = (0, 0, 0)
brown = (121, 25, 5)
tomato = (255, 99, 71)
green = (124, 252, 0)
light_blue = (30, 144, 255)
orang = (255, 69 ,0)
yellow = (255, 215, 0)



# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#Background Image
bgimg = pygame.image.load("graphics/bgimg.JPG")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
#welcome iamge
fgimg = pygame.image.load("graphics/fgimg.JPG")
fgimg = pygame.transform.scale(fgimg, (screen_width, screen_height)).convert_alpha()

goimg = pygame.image.load("graphics/goimg.JPG")
goimg = pygame.transform.scale(goimg, (screen_width, screen_height)).convert_alpha()


#fruit image
apple = pygame.image.load("graphics/apple.png").convert_alpha()
mango = pygame.image.load("graphics/mango.png").convert_alpha()
orange = pygame.image.load("graphics/orange.png").convert_alpha()
straw = pygame.image.load("graphics/straw.png").convert_alpha()
grapes = pygame.image.load("graphics/grapes.png").convert_alpha()
banana = pygame.image.load("graphics/banana.png").convert_alpha()
water = pygame.image.load("graphics/water.png").convert_alpha()
head = pygame.image.load("graphics/snake_head.png").convert_alpha()


# Game Title
pygame.display.set_caption("Odyssey")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont('Ariel', 55)



def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list):
    for x, y in snk_list:
        pygame.draw.ellipse(gameWindow, color, [x, y, 25, 25])

def welcome():
    exit_game = False
    x_pos = 350
    text_x = 350
    color = 'white'
    color2 = light_blue
    flag = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        gameWindow.blit(fgimg, (0, 0))
        frame = pygame.Surface((460, 100))
        frame.fill(color2)
        gameWindow.blit(frame, (x_pos, 460))

        text_screen("Welcome to Fruity Snake", color, text_x, 470)
        text_screen("Press Space Bar To Play", color, text_x, 520)

        if(flag == True):
            text_x -= 1.5
            x_pos -= 1.5
        else:
            x_pos += 1.5
            text_x += 1.5
        if x_pos + 460 == screen_width:
            flag = True
            color = 'white'
            color2 = tomato
        elif x_pos <= 0:
            flag = False
            color = 'white'
            color2 = light_blue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('audio/Nagin Dhun.mp3')
                    pygame.mixer.music.play(-1)
                    gameloop()

        pygame.display.update()
        clock.tick(60)


# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    # Check if hiscore file exists
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20, screen_width - 100)
    food_y = random.randint(20, screen_height - 100)
    score = 0
    init_velocity = 3
    snake_size = 20
    fps = 60
    food = 1
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            gameWindow.blit(goimg, (0, 0))
            text_screen("Press Enter To Continue", white, 250, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        exit_game = True
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_z:
                        score += 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 30 and abs(snake_y - food_y) < 30:
                score += 10
                if food == 1:
                    food = 2
                elif food == 2:
                    food = 3
                elif food == 3:
                    food = 4
                elif food == 4:
                    food = 5
                elif food == 5:
                    food = 6
                elif food == 6:
                    food = 7
                elif food == 7:
                    food = 1
                if score == 80 or score == 400:
                    pygame.mixer.music.load('audio/Dj Nagin.mp3')
                    pygame.mixer.music.play(-1)
                elif score == 160:
                    pygame.mixer.music.load('audio/nagin.mp3')
                    pygame.mixer.music.play(-1)
                elif score == 240:
                    pygame.mixer.music.load('audio/Nagin1.mp3')
                    pygame.mixer.music.play(-1)
                elif score == 320:
                    pygame.mixer.music.load('audio/Twist Nagin.mp3')
                    pygame.mixer.music.play(-1)




                if score % 50 == 0:
                    init_velocity += 0.5



                food_x = random.randint(20, screen_width-100)
                food_y = random.randint(20, screen_height-100)
                snk_length += 5
                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score) + "  HighScore: "+str(hiscore), white, 5, 5)
            #food rectangle
            if food == 1:
                f_surface = pygame.Rect(food_x, food_y, 40, 40)
                gameWindow.blit(apple, f_surface)
                color = tomato
            elif food == 2:
                f_surface = pygame.Rect(food_x, food_y, 40, 40)
                gameWindow.blit(mango, f_surface)
                color = red
            elif food == 3:
                f_surface = pygame.Rect(food_x, food_y, 40, 40)
                gameWindow.blit(orange, f_surface)
                color = yellow
            elif food == 4:
                f_surface = pygame.Rect(food_x, food_y, 80, 80)
                gameWindow.blit(straw, f_surface)
                color = orang
            elif food == 5:
                f_surface = pygame.Rect(food_x, food_y, 60, 60)
                gameWindow.blit(grapes, f_surface)
                color = light_blue
            elif food == 6:
                f_surface = pygame.Rect(food_x, food_y, 40, 40)
                gameWindow.blit(banana, f_surface)
                color = brown
            elif food == 7:
                f_surface = pygame.Rect(food_x, food_y, 80, 80)
                gameWindow.blit(water, f_surface)
                color = white




            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)


            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('audio/sfx-defeat3.mp3')
                pygame.mixer.music.play()

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('audio/sfx-defeat3.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, color, snk_list)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()