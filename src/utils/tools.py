import math
import pygame
from pygame.locals import *

def sine(speed: float, time: int, how_far: float, overall_y: int) -> int:
    """Function to calculate the y position of an object based on a sine wave."""
    t = pygame.time.get_ticks() / 2 % time
    y = math.sin(t / speed) * how_far + overall_y
    return int(y)

def update_background_using_scroll(scroll):
    """Update the background using a scroll effect."""
    scroll += .5
    if scroll > 800:
        scroll = 0
    return scroll

def update_press_key(press_y):
    """Update the position of the press key image."""
    if press_y > 500:
        return press_y * 0.99
    return press_y


def is_close_app_event(event):
    """Check if the event is to close the application."""
    return (event.type == QUIT) or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE)
