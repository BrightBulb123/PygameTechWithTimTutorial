import os
import pygame
import time
import random
import win32api

pygame.font.init()

# Getting the refresh rate of the monitor to set as FPS for Pygame
def getRefreshRate(device):
    settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
    return getattr(settings, 'DisplayFrequency')


device = win32api.EnumDisplayDevices()
REFRESH_RATE = getRefreshRate(device)


# Initializing the main window
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")


# Making some pre-defined colours based on RGB values
COLOURS = {"WHITE": (255, 255, 255), "RED": (255, 0, 0),
           "GREEN": (0, 255, 0),"BLUE": (0, 0, 255),
           "BLACK": (0, 0, 0)}

# Importing the assets

# Spaceships
SPACESHIPS = {
                "YELLOW": os.path.join("assets", "pixel_ship_yellow.png"),
                "RED": os.path.join("assets", "pixel_ship_red_small.png"),
                "GREEN": os.path.join("assets", "pixel_ship_green_small.png"),
                "BLUE": os.path.join("assets", "pixel_ship_blue_small.png")
             }

RED_SPACE_SHIP = pygame.image.load(SPACESHIPS["RED"])  # Enemy
GREEN_SPACE_SHIP = pygame.image.load(SPACESHIPS["GREEN"])  # Enemy
BLUE_SPACE_SHIP = pygame.image.load(SPACESHIPS["BLUE"])  # Enemy
YELLOW_SPACE_SHIP = pygame.image.load(SPACESHIPS["YELLOW"])  # Main Player

# Lasers
LASERS = {
            "YELLOW": os.path.join("assets", "pixel_laser_yellow.png"),
            "RED": os.path.join("assets", "pixel_laser_red.png"),
            "GREEN": os.path.join("assets", "pixel_laser_green.png"),
            "BLUE": os.path.join("assets", "pixel_laser_blue.png")
}

RED_LASER = pygame.image.load(LASERS["RED"])
GREEN_LASER = pygame.image.load(LASERS["GREEN"])
BLUE_LASER = pygame.image.load(LASERS["BLUE"])
YELLOW_LASER = pygame.image.load(LASERS["YELLOW"])

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


class Ship:
    def __init__(self, x, y, health=100) -> None:
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cooldown_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100) -> None:
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = 100


class Enemy(Ship):
    COLOUR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
        }

    def __init__(self, x, y, colour, health=100) -> None:
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOUR_MAP[colour]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y -= vel


def main():
    running = True
    FPS = REFRESH_RATE
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("Fira Code Retina", (35))

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5

    player = Player(300, 650)

    clock = pygame.time.Clock()


    def redraw_window():
        WIN.blit(BG, (0, 0))
        lives_label = main_font.render(f"Lives: {lives}", 1, COLOURS["WHITE"])
        level_label = main_font.render(f"Level: {level}", 1, COLOURS["WHITE"])

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, ((WIDTH-(level_label.get_width()))-10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        pygame.display.update()


    while running:
        clock.tick(FPS)

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for _ in range(wave_length):
                pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and ((player.x - player_vel) > 0):  # Left
            player.x -= player_vel
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (((player.x + player_vel) + player.get_width()) < WIDTH):  # Right
            player.x += player_vel
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and ((player.y - player_vel) > 0):  # Up
            player.y -= player_vel
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (((player.y + player_vel) + player.get_height()) < HEIGHT):  # Down
            player.y += player_vel

        redraw_window()


if __name__ == "__main__":
    main()
