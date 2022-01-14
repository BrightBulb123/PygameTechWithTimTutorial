import os
import pygame
import win32api

# Getting the refresh rate of the monitor to set as FPS for Pygame
def getRefreshRate(device):
    settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
    return getattr(settings, 'DisplayFrequency')


device = win32api.EnumDisplayDevices()
REFRESH_RATE = getRefreshRate(device)

# Initializing the main game window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Test")
FPS = REFRESH_RATE

# Making some pre-defined colours based on RGB values
COLOURS = {"WHITE": (255, 255, 255), "RED": (255, 0, 0),
           "GREEN": (0, 255, 0),"BLUE": (0, 0, 255),
           "BLACK": (0, 0, 0)}

# Importing the assets
SPACESHIPS = {"YELLOW": os.path.join("Assets", "spaceship_yellow.png"),
              "RED": os.path.join("Assets", "spaceship_red.png")}


# Drawing something on the main window (and updating)
def draw_window():
    WIN.fill(COLOURS["white"])
    pygame.display.update()


def main():
    gameClock = pygame.time.Clock()
    run = True
    while run:
        gameClock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
