import os
import pygame
import time
import random
import win32api

# Getting the refresh rate of the monitor to set as FPS for Pygame
def getRefreshRate(device):
    settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
    return getattr(settings, 'DisplayFrequency')


device = win32api.EnumDisplayDevices()
REFRESH_RATE = getRefreshRate(device)

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
BG = pygame.image.load(os.path.join("assets", "background-black.png"))


def main():
    pass


if __name__ == "__main__":
    main()
