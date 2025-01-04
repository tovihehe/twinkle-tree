import random
import pygame
from paths import AUDIO_DIR

class MusicService:
    """Service to manage the music of the game"""
    @staticmethod
    def get_background_music():
        return AUDIO_DIR / "sleigh_ride.ogg"

    @staticmethod
    def start_background_music():
        """Start the background music"""
        if pygame.mixer.music.get_busy():
            return
        music = MusicService.get_background_music()
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
