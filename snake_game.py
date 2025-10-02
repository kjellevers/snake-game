import pygame
import random

# Initializes pygame
pygame.init()

# Constants
GRID_SIZE = 20 # each cell is 20x20 pixels

# Get display info for fullscreen resolution
display_info = pygame.display.Info()
WIDTH = display_info.current_w
HEIGHT = display_info.current_h

GRID_WIDTH = WIDTH // GRID_SIZE 
GRID_HEIGHT = HEIGHT // GRID_SIZE 

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Font for the display
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Food setup
def spawn_food(snake): # generates random postion for food
    while True:
        food = (random.randint(0, GRID_WIDTH -1), random.randint(0, GRID_HEIGHT -1))
        if food not in snake: # keeps trying random positions until it finds one that isnt occupied by the snake
            return food # returns food postion as a tuple (collection of items)

# Reset game setup
def reset_game(): # resets game to its starting state
    global score # allows this funtion to modify the global score variable
    score = 0
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)] # start in the middle of the screen as a single segment
    direction = (1, 0) # means moving right (1 step in x and 0 steps in y) 
    food = spawn_food(snake)
    return snake, direction, food # returns all initial game values 

# Initial game state 
snake, direction, food = reset_game() #initializes game state by calling reset_game function
score = 0 # resets score to 0

# Game loop: boolean flags to control the game loop
running = True # as long as runnng = True the programm exists
game_over = False # when True the snake stops and the game over screen appears

while running: # everything inside this loop runs until running becomes False
    for event in pygame.event.get(): # gets a events e.g (keyboard presses) that happend since the last loop iteration
        if event.type == pygame.QUIT: # if user clicks the x button or closes the window, stop the game
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # if ESC key is pressed, exit the game
                running = False
            elif game_over: # if the game is over and any key is pressed, restart the game
                snake, direction, food = reset_game()
                game_over = False
            else:
            # Normal controls
                if event.key == pygame.K_UP and  direction != (0, 1): # if up arrow is pressed and snake is not moving down
                    direction = (0, -1) # set direction to (0, -1) which means: move up 1 grid cell
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1) # Move down 1 grid cell
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1,0) # Move left 1 grid cell
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0) # Move right 1 grid cell
    
    if not game_over: # only update the snakes position if game is not over
        # Move snake
        head_x, head_y = snake[0] # gets the current position of the snake head (the first element in the snake list)
        new_head =(head_x + direction[0], head_y + direction[1]) # calculates where the new head needs to move by adding the direction vector
        snake.insert(0, new_head) # add new_head position to the front of the snake list
        # Check for collision
        # Hit wall?
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            game_over = True # checks if the new head went out of bounds (hit a wall)

        # Hit itself?
        if new_head in snake[1:]: # Check if head hit any other parts of the body (snake[1:] means all segmenst instead of the head)
            game_over = True

        # Check if snake ate food
        if new_head == food: # f the snake ate the food add 1 to score and spawn new food
            score += 1
            food = spawn_food(snake) 
        # it is important to recongnize that we dont remove the tail here so that the snake grows
        else: # if no food was eaten the last segment (tail) gets removed
            snake.pop() # this creates the illusion of movement - we add a new head and remove the tail

    # Fill background
    screen.fill(BLACK) # clears the entire screen by filling it black, this happens every frame before redrawing everything

    # Draw grid lines 
    for x in range(0, WIDTH, GRID_SIZE): # draws vertical grid lines every GRID_SIZE pixels (range(...) generates 0,20,40,60,...)
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT)) # each line goes from top (x, 0) to bottom (x, HEIGHT)
    for y in range(0, HEIGHT, GRID_SIZE): # draws horizontal grid lines
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

    # Draw snake
    for segment in snake: # loops through every segment of snake
        rect = pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE) # converts grid coordinates to pixel coordinates by multiplying by GRID_SIZE
        pygame.draw.rect(screen, GREEN, rect) # draws a rectangle and draws it in green

    # Draw food
    food_rect = pygame.Rect(food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE) # same thing for the food like with the snake
    pygame.draw.rect(screen, RED, food_rect) # draws the food and draws it in red

    # Draw score
    score_text = small_font.render(f"Score: {score}",True, WHITE) # render() creates a text surface with the score. True means use anti-aliasing (smooth text)
    screen.blit(score_text, (10, 10)) # draws the text at postion(10, 10)

    # Draw game over screen
    if game_over: # creates as Semi-transparent black overlay, this darkens the game screen when you loose
        
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(128) # makes it 50% transparent (0=invisible, 255=solid)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        # Game over text
        game_over_text = font.render("GAME OVER", True, RED) # renders "GAME OVER" in red
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40)) # centers the text at the specified postion, positioned slightly above center because of the -40
        screen.blit(game_over_text, game_over_rect)
        
        # Restart instructions
        restart_text = small_font.render("PRESS ANY KEY TO RESTART", True, WHITE) # similar to game over text but slightly below the center because of the +40
        restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
        screen.blit(restart_text, restart_rect)

    pygame.display.flip() # updates the entire screen with everything that has been drawn/ wtihout this nothing would ever appear on screen
    clock.tick(10) # 10 FPS - controls game speed, higher numbers make the game faster
    
pygame.quit() # shuts the game down when the game loop ends
