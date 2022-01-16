import pygame
import random
import math

# setup display
pygame.init()
WIDTH, HEIGHT = 700, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

# button variables
RADIUS = 25
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 10) / 2)
starty = 135
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 10))
    y = starty + ((i // 10) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('consolas', 30)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('gabriola', 70)

# load images.
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".jpeg")
    images.append(image)

# game variables
hangman_status = 0
words = ["CHOICE", "WORD", "NAME", "COUNTY","TEAMS","FRUIT","JAZZ","WEIRD","CEMETERY","HANGMAN","NOTEBOOK","HELLO","HACKING",
"MICROWAVE","AIRPORT","STATION","ANIMAL","BIRD","ARTICLE","AUTHOR","BALANCE","BATTLE","BILLION","MILLION","BIRTHDAY","BREAKFAST",
"BUSINESS","CARBON","CHOCOLATE","CHRISTMAS","CULTURE","DESTRUCTION","DIALOGUE","DIRECTION","DISCOVERY","ECONOMY","EVOLUTION",
"EXPERIMENT","FABRIC","FAITH","COMPUTER","GHOST","MARKET","MAKEUP","MESSAGE","MODERN","MOUNTAIN","PICTURE","POLLUTION","PRICE",
"PRODUCE","PUNISH","RADICAL","RECIPE","RELATION","SCIENCE","SORRY","TEACHER","TOBACCO","TRAFFIC","UNIQUE","VIRUS","WEAPON","YOUNG"]

word = random.choice(words)
guessed = []

# colors
WHITE = (245,245,245)
BLACK = (0,0,0)
RED = (220,20,60)
BLUE = 	(30,144,255)

#def is the keyword for defining a function. 

def draw():#Draw several simple shapes to a surface.
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("HANGMAN", 1, RED)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    #blit() — blit stands for Block Transfer—and it's going to 
    #copy the contents of one Surface onto another Surface.
    

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (200, 400))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, RED, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)#1 here is used for removing the rough edges(anti-aliasing)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (520, 280))#display hangman images
    pygame.display.update()#update() to make the display Surface actually appear on the user's monitor. 



def main():
    global hangman_status

    FPS = 60 # Frames per second.This Clock object will ensure that our game programs don't run too fast by putting in small pauses on each iteration of the game loop.
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        
        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        
        if won:
            pygame.time.wait(2000)
            screen = pygame.display.set_mode((700, 500))
            WonImage = pygame.image.load("imagewon.png")
            # coordinates of the image
            x = 0
            y = 0
            screen.blit(WonImage, (x, y))
            # paint screen one time
            pygame.display.flip()
            running = True
            while (running): # loop listening for end of game
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

        if hangman_status == 6:
            pygame.time.wait(2000)
            screen = pygame.display.set_mode((700, 500))
            LostImage = pygame.image.load("imagelost.png")
            # coordinates of the image
            x = 0
            y = 0
            screen.blit(LostImage, (x, y))
            # paint screen one time
            pygame.display.flip()
            running = True
            while (running): # loop listening for end of game
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
    
while True:
    
    main()
pygame.quit()
