import pygame
from src.components.game_status import GameStatus
from src.config import Config
from src.game_phases import main_menu_phase, gameplay_phase, end_background_phase, exit_game_phase
from src.global_state import GlobalState
from src.services.music_service import MusicService

# Initialize Pygame
pygame.init()

# Set the clock, which will be used to control the frame rate
FramePerSec = pygame.time.Clock()

def update_game_display():
    """Update the game display"""
    pygame.display.update()
    FramePerSec.tick(Config.FPS)


def main():
    """Main function of the game"""
    while True:
        if GlobalState.GAME_STATE == GameStatus.MAIN_MENU:
            main_menu_phase()
        elif GlobalState.GAME_STATE == GameStatus.GAMEPLAY:
            gameplay_phase()
        elif GlobalState.GAME_STATE == GameStatus.END_BACKGROUND:
            end_background_phase()
        elif GlobalState.GAME_STATE == GameStatus.GAME_END:
            exit_game_phase()

        MusicService.start_background_music()
        update_game_display()


if __name__ == "__main__":
    main()
