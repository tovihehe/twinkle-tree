from enum import Enum

class GameStatus(Enum):
    """Game status enumeration"""
    MAIN_MENU = 0
    GAMEPLAY = 1
    END_BACKGROUND = 2
    GAME_END = 3