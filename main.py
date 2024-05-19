import pygame
import sys
import constants as CONSTANTS
from sprite import Sprite


def get_movement(event, key=None):
    player_speed_y = 0
    player_speed_x = 0

    if event == pygame.QUIT:
        running = False

    elif event == pygame.KEYDOWN:
        if key == pygame.K_UP:
            player_speed_y = -CONSTANTS.PLAYER_SPEED
        elif key == pygame.K_DOWN:
            player_speed_y = CONSTANTS.PLAYER_SPEED
        elif key == pygame.K_LEFT:
            player_speed_x = -CONSTANTS.PLAYER_SPEED
        elif key == pygame.K_RIGHT:
            player_speed_x = CONSTANTS.PLAYER_SPEED

    elif event == pygame.KEYUP:
        if key == pygame.K_UP or key == pygame.K_DOWN:
            player_speed_y = 0
        elif key == pygame.K_LEFT or key == pygame.K_RIGHT:
            player_speed_x = 0

    return player_speed_x, player_speed_y


def main():
    pygame.init()

    screen = pygame.display.set_mode((CONSTANTS.SCREEN_WIDTH, CONSTANTS.SCREEN_HEIGHT))

    player_x = CONSTANTS.SCREEN_WIDTH // 2
    player_y = CONSTANTS.SCREEN_HEIGHT // 2
    player_speed_x = 0
    player_speed_y = 0

    main_sprite = Sprite(
        player_x,
        player_y,
        CONSTANTS.PLAYER_SIZE,
        CONSTANTS.PLAYER_SIZE,
        CONSTANTS.COLOR_PLAYER,
        {"idle": "image/Sprite-Idle.png", "walk": "image/Sprite-Walking.png"},
    )

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
                player_speed_x, player_speed_y = get_movement(
                    event=event.type, key=event.key
                )

        player_x += player_speed_x
        player_y += player_speed_y

        screen.fill(CONSTANTS.COLOR_BACKGROUND)

        main_sprite.set_pos(player_x, player_y)
        main_sprite.draw(screen)

        pygame.display.flip()

        clock.tick(CONSTANTS.FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
