import pygame
import math
import random

pygame.init()
pygame.mixer.init()

scores = []

# Create game window
SCREEN_HEIGHT, SCREEN_WIDTH = 700, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Background Music
pygame.mixer.music.load('music/christmas-party.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

background = pygame.image.load('images/background.png')
prompt = pygame.image.load('images/prompt.png')

def render_background():
    screen.blit(background, (0, 0))

def render_prompt():
    screen.blit(prompt, (SCREEN_WIDTH // 2 - prompt.get_width() // 2, 590))

def render_score():
    # Display score
    scoreCard = pygame.image.load('images/score-card.png')
    screen.blit(scoreCard, (SCREEN_WIDTH // 2 - scoreCard.get_width() // 2, 220))

    font_path = 'font/ConcertOne-Regular.ttf'
    font = pygame.font.Font(font_path, 35)
    score_text = font.render(f"Final Score: {current_score}", True, black)
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 320))

    scores.append(current_score)

    if scores:
        highest_score = max(scores)
        highest_score_text = font.render(f"High Score: {highest_score}", True, black)
        screen.blit(highest_score_text, (SCREEN_WIDTH // 2 - highest_score_text.get_width() // 2, 380))

running = True
black = (0,0,0)

# Title screen
def title_screen():
    global running
    angle = 0 

    while running:
        render_background()

        title = pygame.image.load('images/title.png')
        title_x = SCREEN_WIDTH // 2 - title.get_width() // 2
        title_y = 50
        base_y = title_y

        '''Title animation'''
        speed = 2  # Speed of the animation
        amplitude = 20  # Max distance up and down

        angle += speed  # Increment the angle
        title_y = base_y + amplitude * math.sin(math.radians(angle))

        if angle >= 360:
            angle -= 360

        # Draw title image
        screen.blit(title, (title_x, title_y))
        clock.tick(60)

        mug = pygame.image.load('images/mug.png')
        screen.blit(mug, (SCREEN_WIDTH // 2 - mug.get_width() // 2 + 20, SCREEN_HEIGHT // 2 - mug.get_height() // 2 + 50))

        render_prompt()

        pygame.display.update()

        #Wait for key press
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                return

# Instructions
def instructions():
    global running
    while True:
        render_background()

        instuction_title = pygame.image.load('images/instruction-title.png')
        screen.blit(instuction_title, (SCREEN_WIDTH //2 - instuction_title.get_width()//2, 10))
        
        text_box = pygame.image.load('images/text-box.png')
        screen.blit(text_box, (SCREEN_WIDTH //2 - text_box.get_width()//2, 100))

        render_prompt()

        pygame.display.update()

        #Wait for key press
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                return

#Ingredient images
ingredientImgs = [
    pygame.image.load('images/good-ingredients/item-1.png'),
    pygame.image.load('images/good-ingredients/item-2.png'),
    pygame.image.load('images/good-ingredients/item-4.png'),
    pygame.image.load('images/good-ingredients/item-5.png'),
    pygame.image.load('images/good-ingredients/item-6.png'),
    pygame.image.load('images/bad-ingredients/item-1.png'),
    pygame.image.load('images/bad-ingredients/item-2.png'),
    pygame.image.load('images/bad-ingredients/item-3.png'),
    pygame.image.load('images/bad-ingredients/item-4.png'),
]

def set_ingredient():
    # Choose a random ingredient
    ingredient = random.choice(ingredientImgs)

    # Tag the ingredient type
    if ingredient in ingredientImgs[-4:]:
        ingredient_type = "bad"
    else:
        ingredient_type = "good"

    x = random.randint(3, 300)  # Random x position across the screen width
    y = random.randint(-200, -50)  # Start above the screen
    speed = random.uniform(2, 5)  # Random speed

    return {"img": ingredient, "x": x, "y": y, "speed": speed, "type": ingredient_type}

def game_over():
    gameOverImg = pygame.image.load('images/game-over.png')
    screen.blit(gameOverImg, (SCREEN_WIDTH // 2 - gameOverImg.get_width() // 2, 120))

    render_score()
    render_prompt()
    reset_game()

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                return  # Exit the game over screen

def reset_game():
    """Reset game state variables and restart background music."""
    global playerX, playerY, playerX_change, count, current_score

    # Reset player position and obstacle
    playerX = SCREEN_WIDTH // 2 - playerImg.get_width()//2
    playerY = 550
    playerX_change = 0

    # Reset the score
    count = 0
    current_score = 0


# Player image and positions
playerImg = pygame.transform.scale(pygame.image.load("images/mug-2.png"),(150,150))
playerX = SCREEN_WIDTH // 2 - playerImg.get_width()//2
playerY = 550
playerX_change = 0

def player(playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))

def main_game():
    global running, playerX, playerY, playerX_change, playerImg, count, current_score, font_path
    ingredients = [set_ingredient() for _ in range(3)]

    font_path = 'font/ConcertOne-Regular.ttf'

    count = 0
    current_score = 0
    clock = pygame.time.Clock()

    original_player_img = pygame.transform.scale(pygame.image.load("images/mug-2.png"),(150,150))
    playerImg = original_player_img  # Save the original player image

    while running:
        render_background()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Player movement on key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -8
                elif event.key == pygame.K_RIGHT:
                    playerX_change = 8

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # Draw player
        player(playerX, playerY)

        # Update player position
        playerX += playerX_change

        # Prevent player from moving off screen
        if playerX <= 0:
            playerX = 0
        elif playerX >= SCREEN_WIDTH - playerImg.get_width():
            playerX = SCREEN_WIDTH - playerImg.get_width()
        
        player_rect = pygame.Rect(playerX, playerY, playerImg.get_width(), playerImg.get_height())  # Player's bounding box
        
        # Update and draw each ingredient
        for ingredient in ingredients:
            ingredient["y"] += ingredient["speed"]  # Move ingredient down
            screen.blit(ingredient["img"], (ingredient["x"], ingredient["y"]))

            # Ingredient bounding box
            ingredient_rect = pygame.Rect(
                ingredient["x"], ingredient["y"],
                ingredient["img"].get_width(),
                ingredient["img"].get_height()
            )

            # Check collision
            if player_rect.colliderect(ingredient_rect):
                if ingredient["type"] == "bad":  # Check if bad ingredient
                    count += 1
                    current_score -= 100
                    if count > 2:
                        game_over()
                    else:
                        playerImg = pygame.transform.scale(pygame.image.load("images/mug-shocked.png"),(150,150))  # Change player image
                        player(playerX, playerY)
                        pygame.display.update()
                        pygame.time.delay(200)  # Show the new image for 0.2 seconds
                        playerImg = original_player_img  # Restore original image
                
                if ingredient["type"] == "good":
                    current_score +=200

                # Remove collided ingredient and spawn a new one
                ingredients.remove(ingredient)
                ingredients.append(set_ingredient())

            # Reset ingredient if it falls below the screen
            if ingredient["y"] > SCREEN_HEIGHT:
                ingredients.remove(ingredient)
                ingredients.append(set_ingredient())

        current_score += 1
        font = pygame.font.Font(font_path, 40)
        score_text = font.render(f"Score: {current_score}", True, black)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)

while running:
    title_screen()
    instructions()
    if running:  
        main_game()
pygame.quit()