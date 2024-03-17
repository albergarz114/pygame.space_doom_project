import pygame  # 1st step import
import time    # 1st step import 
import random  # 1st step import 

pygame.font.init()

# MOVEMENTS
# COLLISIONS
# PROJECTILES
# BACKGROUNDS





WIDTH, HEIGHT = 1000, 800 # 2nd step CREATE A WINDOW
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # 2nd step CREATE A WINDOW
pygame.display.set_caption("Space Doom")  # 2nd step CREATE A WINDOW

BG = pygame.transform.scale(pygame.image.load("blue_space.jpg"), (WIDTH, HEIGHT)) #3 step : add Background 

PLAYER_WIDTH = 40  ##4 step: Moving Character
PLAYER_HEIGHT = 60  ##4 step: Moving Character
PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3
FONT = pygame.font.SysFont("comicsans", 30)


def draw(player, elapsed_time, stars): #3 step : add Background 
    WIN.blit(BG, (0, 0)) #3 step : add Background #

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10,10))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)
    
    pygame.display.update() #3 step : add Background 



def main():  
    run = True # 2nd step CREATE A WINDOW

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)  ##4 step: Moving Character

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0
    stars = []
    hit = False



    while run:  #game loop
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT,STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200,star_add_increment - 50)
            star_count = 0
        
        
        for event in pygame.event.get():  # 2nd step CREATE A WINDOW 
            if event.type == pygame.QUIT: # 2nd step CREATE A WINDOW
                run = False # 2nd step CREATE A WINDOW
                break # 2nd step CREATE A WINDOW
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        #if keys[pygame.K_UP] and player.y - PLAYER_VEL >= 0:
        #    player.y -= PLAYER_VEL
        #if keys[pygame.K_DOWN] and player.y + PLAYER_VEL + player.height <= HEIGHT:
        #    player.y += PLAYER_VEL
            
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break


        if hit:
            lost_text = FONT.render("Du hast das Spiel verloren!", 1, "red")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        
        draw(player, elapsed_time, stars)

    pygame.quit()  # 2nd step CREATE A WINDOW

if __name__ == "__main__":  # 2nd step CREATE A WINDOW
    main()  # 2nd step CREATE A WINDOW


