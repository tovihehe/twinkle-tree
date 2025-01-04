import pygame
from paths import ASSETS_DIR, MENU_DIR
from src.config import Config
from src.utils.tools import sine


class VisualizationService:
    """Service to manage the visualization of the game"""
    @staticmethod
    def get_background_image():
        return pygame.image.load(ASSETS_DIR / "bg1.png").convert_alpha()

    @staticmethod
    def get_title_image():
        return pygame.image.load(MENU_DIR / "title.png").convert_alpha()
    
    @staticmethod
    def get_tree_icon():
        return pygame.image.load(MENU_DIR / "tree.png").convert_alpha()
    
    @staticmethod
    def get_end_title_image():
        return pygame.image.load(ASSETS_DIR / "xmas.png").convert_alpha()

    @staticmethod  
    def get_tree_image():
        return pygame.image.load(ASSETS_DIR / "treedeco.png").convert_alpha()
    
    @staticmethod
    def get_tree_colored_images():
        return [
            pygame.image.load(ASSETS_DIR / "treedeco_lights1.png").convert_alpha(),
            pygame.image.load(ASSETS_DIR / "treedeco_lights2.png").convert_alpha(),
            pygame.image.load(ASSETS_DIR / "treedeco_lights3.png").convert_alpha(),
        ]
    
    @staticmethod
    def get_press_key_image():
        return pygame.image.load(MENU_DIR / "press_key.png").convert_alpha()

    @staticmethod
    def get_grass_image():
        return pygame.image.load(ASSETS_DIR / "grass.png").convert_alpha()
    
    @staticmethod
    def get_snowman_image():
        return pygame.image.load(ASSETS_DIR / "snowman.png").convert_alpha()
    
    @staticmethod
    def get_button_image():
        return pygame.image.load(ASSETS_DIR / "button.png").convert_alpha()
    
    @staticmethod
    def get_button_hover_image():
        return pygame.image.load(ASSETS_DIR / "button_hover.png").convert_alpha()
    
    @staticmethod
    def get_button_pushed_image():
        return pygame.image.load(ASSETS_DIR / "button_pushed.png").convert_alpha()
    
    @staticmethod
    def get_main_font():
        return pygame.font.Font(ASSETS_DIR / "VCR_OSD_MONO_1.001.ttf", 40)

    @staticmethod
    def get_credit_font_font():
        return pygame.font.Font(ASSETS_DIR / "BaiJamjuree-Bold.ttf", 12)

    @staticmethod
    def load_main_game_displays():
        """Load the upper title and the icon of the game."""
        pygame.display.set_caption("Twinkle Tree")
        tree = VisualizationService.get_tree_icon()
        pygame.display.set_icon(tree)

    @staticmethod
    def draw_background_with_scroll(screen, scroll):
        """Draw the background with a scroll effect."""
        background = VisualizationService.get_background_image()
        screen.blit(background, (0, scroll))
        screen.blit(background, (0, scroll - Config.HEIGHT))

    @staticmethod
    def draw_author_credits(screen):
        """Draw the author credits."""
        credit_font = VisualizationService.get_credit_font_font()
        author_credits = credit_font.render("©TOVI 2024", True, (0, 0, 0))
        credits_rect = author_credits.get_rect(center=(Config.WIDTH // 2, 750))
        screen.blit(author_credits, credits_rect)

    @staticmethod
    def draw_title(screen):
        """Draw the title of the game."""
        y = sine(200.0, 1280, 10.0, 100)
        title = VisualizationService.get_title_image()
        screen.blit(title, (260, y))

    @staticmethod
    def draw_end_title(screen):
        """Draw the end title of the game."""
        y = sine(200.0, 1280, 10.0, 100)
        end_title = VisualizationService.get_end_title_image()
        screen.blit(end_title, (340, y))

    @staticmethod
    def draw_press_key(screen, press_y):
        """Draw the press key image."""
        press_key = VisualizationService.get_press_key_image()
        screen.blit(press_key, (400, press_y))

    @staticmethod
    def draw_grass(screen):
        """Draw the grass."""
        grass = VisualizationService.get_grass_image()
        screen.blit(grass, (-10, 715))

    @staticmethod
    def draw_snowman(screen):
        """Draw the snowman."""
        snowman = VisualizationService.get_snowman_image()
        screen.blit(snowman, (40, 490))

    @staticmethod
    def draw_tree(screen, button):
        """Draw the tree with changing lights."""
        tree_images = VisualizationService.get_tree_colored_images()
        tree_image = (tree_images[button.current_light_image] 
                    if button.lights else 
                    VisualizationService.get_tree_image())
        screen.blit(tree_image, (675, 130)) 

    @staticmethod
    def draw_thanks_message(screen):
        """Draw the thanks message."""
        font = VisualizationService.get_main_font()
        text_surface = font.render("Thank You for Playing!", True, "Black")
        screen.blit(text_surface, (360, 600)) 

    @staticmethod
    def draw_main_menu(screen, press_y):
        """Draw the main menu of the game."""
        VisualizationService.draw_author_credits(screen)
        VisualizationService.draw_title(screen)
        VisualizationService.draw_press_key(screen, press_y)

    @staticmethod
    def draw_gameplay_background_with_scroll(screen, scroll, button):
        """Draw the gameplay background with scroll."""
        VisualizationService.draw_background_with_scroll(screen, scroll)
        VisualizationService.draw_grass(screen)
        VisualizationService.draw_snowman(screen)
        VisualizationService.draw_tree(screen, button)

    @staticmethod
    def draw_end_background(screen, scroll):
        """Draw the ending background."""
        VisualizationService.draw_background_with_scroll(screen, scroll)
        VisualizationService.draw_end_title(screen)
        VisualizationService.draw_thanks_message(screen)
        VisualizationService.draw_author_credits(screen)
