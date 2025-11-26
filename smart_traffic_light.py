import pygame
pygame.init()
screen = pygame.display.set_mode((300,650))
clock = pygame.time.Clock()
FPS = 60

running = True
state = "RED"
state_start_time = pygame.time.get_ticks()
RED_TIME = 5000
YELLOW_TIME = 2000
GREEN_TIME = 4000

def draw_traffic_light(state):
    pygame.draw.rect(screen, (0,0,0), (110, 225, 80, 250), border_radius=10)
    
    # 
    red_on, red_off = (255,0,0), (100,0,0)
    yellow_on, yellow_off = (255,255,0), (100,100,0)
    green_on, green_off = (0,255,0), (0,100,0)

    red_color = red_on if state == "RED" else red_off
    pygame.draw.circle(screen, red_color, (150, 275), 30)
    
    yellow_color = yellow_on if state == "YELLOW" else yellow_off
    pygame.draw.circle(screen, yellow_color, (150, 350), 30)
    
    green_color = green_on if state == "GREEN" else green_off
    pygame.draw.circle(screen, green_color, (150, 425), 30)

while running:
    bg_fill = (200,200,200)
    screen.fill(bg_fill)
    draw_traffic_light(state)

    current_time = pygame.time.get_ticks()

    if state == "RED" and current_time - state_start_time >= RED_TIME:
        state = "GREEN"
        state_start_time = current_time
    elif state == "GREEN" and current_time - state_start_time >= GREEN_TIME:
        state = "YELLOW"
        state_start_time = current_time
    elif state == "YELLOW" and current_time - state_start_time >= YELLOW_TIME:
        state = "RED"
        state_start_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()