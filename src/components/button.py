import pygame
from src.services.visualization_service import VisualizationService

class Button:
    """Button class to handle the button events and rendering."""
    def __init__(self, x, y):
        self.default_image = VisualizationService.get_button_image()
        self.hover_image = VisualizationService.get_button_hover_image()
        self.pressed_image = VisualizationService.get_button_pushed_image()
        self.rect = self.default_image.get_rect()
        self.rect.topleft = (x, y)
        self.state = "default"
        self.lights = False
        self.last_switch_time = pygame.time.get_ticks()  # Time of the last image switch
        self.current_light_image = 0  # Index of the current light image

    def handle_event(self, event):
        """Change the button state based on the event."""
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if self.rect.collidepoint(mouse_pos):
            if mouse_click[0] == 1 and self.state != "pressed":
                print("Button clicked")
                self.state = "pressed"
                self.lights = not self.lights  

            elif mouse_click[0] == 0:
                self.state = "hover"
        else:
            self.state = "default"

    def update_lights(self):
        """Update the light image if enough time has passed."""
        if self.lights:  # Change colors only when lights are on
            current_time = pygame.time.get_ticks()
            if current_time - self.last_switch_time >= 1000:  # 1000ms = 1 second
                self.last_switch_time = current_time
                self.current_light_image = (self.current_light_image + 1) % 3  # Cycle through 3 images

    def draw(self, screen):
        """Draw the button based on its state."""
        if self.state == "default":
            screen.blit(self.default_image, self.rect.topleft)
        elif self.state == "hover":
            screen.blit(self.hover_image, self.rect.topleft)
        elif self.state == "pressed":
            screen.blit(self.pressed_image, self.rect.topleft)
