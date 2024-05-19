import pygame
import sys
import constants as CONSTANTS
from sprite import Sprite

currently_moving = [False, False, False, False]


def handle_move_events(event, key=None):
    global currently_moving

    if event.type == pygame.KEYDOWN:
        if key == pygame.K_UP:
            currently_moving[0] = True
        elif key == pygame.K_DOWN:
            currently_moving[1] = True
        elif key == pygame.K_LEFT:
            currently_moving[2] = True
        elif key == pygame.K_RIGHT:
            currently_moving[3] = True
    elif event.type == pygame.KEYUP:
        if key == pygame.K_UP:
            currently_moving[0] = False
        elif key == pygame.K_DOWN:
            currently_moving[1] = False
        elif key == pygame.K_LEFT:
            currently_moving[2] = False
        elif key == pygame.K_RIGHT:
            currently_moving[3] = False


def get_movement():
    global currently_moving
    player_speed_y = 0
    player_speed_x = 0

    if currently_moving[0] and not currently_moving[1]:
        player_speed_y = -CONSTANTS.PLAYER_SPEED
    elif currently_moving[1] and not currently_moving[0]:
        player_speed_y = CONSTANTS.PLAYER_SPEED
    if currently_moving[2] and not currently_moving[3]:
        player_speed_x = -CONSTANTS.PLAYER_SPEED
    elif currently_moving[3] and not currently_moving[2]:
        player_speed_x = CONSTANTS.PLAYER_SPEED

    return player_speed_x, player_speed_y


player_velocity_x = 0
player_velocity_y = 0


def main():
    global player_velocity_x, player_velocity_y

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
        image_width=200,
        image_height=200,
        animate_frames=50,
        initial_state="idle",
    )

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                handle_move_events(event, event.key)

        player_speed_x, player_speed_y = get_movement()

        player_velocity_x += player_speed_x
        player_velocity_y += player_speed_y

        player_velocity_x *= CONSTANTS.PLAYER_FRICTION
        player_velocity_y *= CONSTANTS.PLAYER_FRICTION

        player_velocity_x = min(
            max(player_velocity_x, -CONSTANTS.PLAYER_MAX_VELOCITY),
            CONSTANTS.PLAYER_MAX_VELOCITY,
        )
        player_velocity_y = min(
            max(player_velocity_y, -CONSTANTS.PLAYER_MAX_VELOCITY),
            CONSTANTS.PLAYER_MAX_VELOCITY,
        )

        player_x += player_velocity_x
        player_y += player_velocity_y

        screen.fill(CONSTANTS.COLOR_BACKGROUND)

        main_sprite.set_pos(player_x, player_y)
        main_sprite.draw(screen)
        main_sprite.animate()

        if player_speed_x != 0 or player_speed_y != 0:
            main_sprite.set_state("walk")
        else:
            main_sprite.set_state("idle")

        pygame.display.flip()

        clock.tick(CONSTANTS.FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
