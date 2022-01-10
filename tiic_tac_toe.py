import pygame

def up_left():
    pygame.draw.line(game_screen, (0,255,0), (100,100), (100,196), width=4)
    pygame.draw.line(game_screen, (0,255,0), (100,196), (196,196), width=4)
    pygame.draw.line(game_screen, (0,255,0), (196,196), (196,100), width=4)
    pygame.draw.line(game_screen, (0,255,0), (196,100), (100,100), width=4)
def up_center():
    pygame.draw.line(game_screen, (0,255,0), (204,100), (204,196), width=4)
    pygame.draw.line(game_screen, (0,255,0), (204,196), (296,196), width=4)
    pygame.draw.line(game_screen, (0,255,0), (296,196), (296,100), width=4)
    pygame.draw.line(game_screen, (0,255,0), (296,100), (204,100), width=4)
def up_right():
    pygame.draw.line(game_screen, (0,255,0), (304,100), (304,196), width=4)
    pygame.draw.line(game_screen, (0,255,0), (304,196), (400,196), width=4)
    pygame.draw.line(game_screen, (0,255,0), (400,196), (400,100), width=4)
    pygame.draw.line(game_screen, (0,255,0), (400,100), (304,100), width=4)
def middle_left():
    pygame.draw.line(game_screen, (0,255,0), (100,204), (100,296), width=4)
    pygame.draw.line(game_screen, (0,255,0), (100,296), (196,296), width=4)
    pygame.draw.line(game_screen, (0,255,0), (196,296), (196,204), width=4)
    pygame.draw.line(game_screen, (0,255,0), (196,204), (100,204), width=4)
def middle_center():
    pygame.draw.line(game_screen, (0,255,0), (204,204), (204,296), width=4)
    pygame.draw.line(game_screen, (0,255,0), (204,204), (296,204), width=4)
    pygame.draw.line(game_screen, (0,255,0), (296,296), (296,204), width=4)
    pygame.draw.line(game_screen, (0,255,0), (296,296), (204,296), width=4)
def middle_right():
    pygame.draw.line(game_screen, (0,255,0), (304,204), (304,296), width=4)
    pygame.draw.line(game_screen, (0,255,0), (304,296), (400,296), width=4)
    pygame.draw.line(game_screen, (0,255,0), (400,296), (400,204), width=4)
    pygame.draw.line(game_screen, (0,255,0), (400,204), (304,204), width=4)
def lower_center():
    pygame.draw.line(game_screen, (0,255,0), (204,304), (204,400), width=4)
    pygame.draw.line(game_screen, (0,255,0), (204,400), (296,400), width=4)
    pygame.draw.line(game_screen, (0,255,0), (296,400), (296,304), width=4)
    pygame.draw.line(game_screen, (0,255,0), (296,304), (204,304), width=4)
def lower_left():
    pygame.draw.line(game_screen, (0,255,0), (100,304), (100,400), width=4)
    pygame.draw.line(game_screen, (0,255,0), (100,400), (196,400), width=4)
    pygame.draw.line(game_screen, (0,255,0), (196,400), (196,304), width=4)
    pygame.draw.line(game_screen, (0,255,0), (196,304), (100,304), width=4)
def lower_right():
    pygame.draw.line(game_screen, (0, 255, 0), (304, 304), (304, 400), width=4)
    pygame.draw.line(game_screen, (0, 255, 0), (304, 400), (396, 400), width=4)
    pygame.draw.line(game_screen, (0, 255, 0), (396, 400), (396, 304), width=4)
    pygame.draw.line(game_screen, (0, 255, 0), (396, 304), (304, 304), width=4)
def pos(position):
    if position == 1:
        up_left()
    elif position == 2:
        up_center()
    elif position == 3:
        up_right()
    elif position == 4:
        middle_left()
    elif position == 5:
        middle_center()
    elif position == 6:
        middle_right()
    elif position == 7:
        lower_left()
    elif position == 8:
        lower_center()
    elif position == 9:
        lower_right()

game_over = False
game_exit = False
position = 5
f = [0,0,0,0,0,0,0,0,0]
a = 1
cross = pygame.image.load("D:\\Coading Ninjas\\Tic Tac Toe\\cross.png")
circle = pygame.image.load("D:\\Coading Ninjas\\Tic Tac Toe\\circle.png")
cross_won = pygame.image.load("D:\\Coading Ninjas\\Tic Tac Toe\\Cross won.png")
circle_won = pygame.image.load("D:\\Coading Ninjas\\Tic Tac Toe\\circle won.png")
while game_exit == False:
    game_screen = pygame.display.set_mode((500, 500))
    game_screen.fill((255,252,208))
    pygame.draw.line(game_screen, (0,0,0), (200,100), (200,400), width=4)
    pygame.draw.line(game_screen, (0,0,0), (300,100), (300,400), width=4)
    pygame.draw.line(game_screen, (0,0,0), (100,200), (400,200), width=4)
    pygame.draw.line(game_screen, (0,0,0), (100,300), (400,300), width=4)
    m=0
    while m<9:
        if f[m] == 1:
            p = m+1
            if p == 1:
                game_screen.blit(cross,(100, 100))
            elif p == 2:
                game_screen.blit(cross,(200, 100))
            elif p == 3:
                game_screen.blit(cross,(300, 100))
            elif p == 4:
                game_screen.blit(cross,(100, 200))
            elif p == 5:
                game_screen.blit(cross,(200, 200))
            elif p == 6:
                game_screen.blit(cross,(300, 200))
            elif p == 7:
                game_screen.blit(cross,(100, 300))
            elif p == 8:
                game_screen.blit(cross,(200, 300))
            elif p == 9:
                game_screen.blit(cross,(300, 300))
        elif f[m] == 2:
            p = m + 1
            if p == 1:
                game_screen.blit(circle, (100, 100))
            elif p == 2:
                game_screen.blit(circle, (200, 100))
            elif p == 3:
                game_screen.blit(circle, (300, 100))
            elif p == 4:
                game_screen.blit(circle, (100, 200))
            elif p == 5:
                game_screen.blit(circle, (200, 200))
            elif p == 6:
                game_screen.blit(circle, (300, 200))
            elif p == 7:
                game_screen.blit(circle, (100, 300))
            elif p == 8:
                game_screen.blit(circle, (200, 300))
            elif p == 9:
                game_screen.blit(circle, (300, 300))
        m += 1
    if (f[0] == f[1]) and (f[1] == f[2]) and f[0] != 0:
        if f[0]==1:
            game_screen.blit(cross_won,(150, 20))
            game_over = True
        elif f[0] == 2:
            game_screen.blit(circle_won,(150, 20))
            game_over = True
    elif (f[3] == f[4]) and (f[4] == f[5]) and f[3] != 0:
        if f[3]==1:
            game_screen.blit(cross_won,(150, 20))
            game_over = True
        elif f[3] == 2:
            game_screen.blit(circle_won,(150, 20))
            game_over = True
    elif (f[6] == f[7]) and (f[7] == f[8]) and f[6] != 0:
        if f[6]==1:
            game_screen.blit(cross_won,(150, 20))
            game_over = True
        elif f[6] == 2:
            game_screen.blit(circle_won,(150, 20))
            game_over = True
    elif (f[0] == f[3]) and (f[3] == f[6]) and f[0] != 0:
        if f[0]==1:
            game_screen.blit(cross_won,(150, 20))
            game_over = True
        elif f[0] == 2:
            game_screen.blit(circle_won,(150, 20))
            game_over = True
    elif (f[1] == f[4]) and (f[4] == f[7]) and f[1] != 0:
        if f[1]==1:
            game_screen.blit(cross_won,(150, 20))
            game_over = True
        elif f[1] == 2:
            game_screen.blit(circle_won,(150, 20))
            game_over = True
    elif (f[2] == f[5]) and (f[5] == f[8]) and f[2] != 0:
        if f[2]==1:
            game_screen.blit(cross_won,(150, 20))
            game_over = True
        elif f[2] == 2:
            game_screen.blit(circle_won,(150, 20))
            game_over = True
    elif (f[0] == f[4]) and (f[4] == f[8]) and f[0] != 0:
        if f[0]==1:
            game_screen.blit(cross_won,(150, 20))
            game_over = True
        elif f[0] == 2:
            game_screen.blit(circle_won,(150, 20))
            game_over = True
    elif (f[2] == f[4]) and (f[4] == f[6]) and f[2] != 0:
        if f[2]==1:
            game_screen.blit(cross_won,(150, 20))
            game_over = True
        elif f[2] == 2:
            game_screen.blit(circle_won,(150, 20))
            game_over = True
    elif (f[0] == f[1]) and (f[1] == f[2]) and f[0] != 0:
        if f[0]==1:
            game_screen.blit(cross_won,(150, 20))
            game_over = True
        elif f[0] == 2:
            game_screen.blit(circle_won,(150, 20))
            game_over = True
    elif (f[0] == f[1]) and (f[1] == f[2]) and f[0] != 0:
        if f[0]==1:
            game_screen.blit(cross_won,(150, 20))
            game_over = True
        elif f[0] == 2:
            game_screen.blit(circle_won,(150, 20))
            game_over = True
    elif (f[0] == f[1]) and (f[1] == f[2]) and f[0] != 0:
        if f[0]==1:
            game_screen.blit(cross_won,(150, 20))
            game_over = True
        elif f[0] == 2:
            game_screen.blit(circle_won,(150, 20))
            game_over = True
    elif (f[0] != 0 and f[1] != 0 and f[2] != 0 and f[3] != 0 and f[4] != 0 and f[5] != 0 and f[6] != 0 and f[7] != 0 and f[8] != 0):
        game_over = True
    pos(position)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if (position==1 or position == 2 or position == 3):
                    pass
                elif (position == 4):
                    position = 1
                elif (position == 5):
                    position = 2
                elif (position == 6):
                    position = 3
                elif (position == 7):
                    position = 4
                elif (position == 8):
                    position = 5
                elif (position == 9):
                    position = 6
            if event.key == pygame.K_DOWN:
                if (position==7 or position == 8 or position == 9):
                    pass
                elif (position == 1):
                    position = 4
                elif (position == 2):
                    position = 5
                elif (position == 3):
                    position = 6
                elif (position == 4):
                    position = 7
                elif (position == 5):
                    position = 8
                elif (position == 6):
                    position = 9
            if event.key == pygame.K_RIGHT:
                if (position==3 or position == 6 or position == 9):
                    pass
                elif (position == 1):
                    position = 2
                elif (position == 2):
                    position = 3
                elif (position == 4):
                    position = 5
                elif (position == 5):
                    position = 6
                elif (position == 7):
                    position = 8
                elif (position == 8):
                    position = 9
            if event.key == pygame.K_LEFT:
                if (position==1 or position == 4 or position == 7):
                    pass
                elif (position == 2):
                    position = 1
                elif (position == 3):
                    position = 2
                elif (position == 5):
                    position = 4
                elif (position == 6):
                    position = 5
                elif (position == 8):
                    position = 7
                elif (position == 9):
                    position = 8
            if event.key == pygame.K_RETURN:
                if (game_over == True):
                    f = [0,0,0,0,0,0,0,0,0]
                    game_over = False
                elif (a%2 == 1 and f[(position-1)]==0):
                    f[(position-1)]=1
                    a+=1
                elif (a%2 == 0 and f[(position-1)]==0):
                    f[(position-1)]=2
                    a+=1
    pygame.display.update()
