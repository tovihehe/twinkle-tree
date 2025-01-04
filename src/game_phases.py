import pygame
import sys
from src.components.game_status import GameStatus
from src.components.button import Button
from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from src.services.dialog_service import Dialog
from src.utils.tools import update_background_using_scroll, update_press_key, is_close_app_event
GlobalState.load_main_screen()
VisualizationService.load_main_game_displays()

# Define the button object
button = Button(720, 720)

def main_menu_phase():
    """Render the main menu of the game."""
    events = pygame.event.get()

    for event in events:
        if is_close_app_event(event):
            GlobalState.GAME_STATE = GameStatus.GAME_END
            return

        if event.type == pygame.KEYDOWN:
            GlobalState.GAME_STATE = GameStatus.GAMEPLAY

    # Background rendering
    GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL)
    VisualizationService.draw_background_with_scroll(GlobalState.SCREEN, GlobalState.SCROLL)

    # Press key image rendering
    GlobalState.PRESS_Y = update_press_key(GlobalState.PRESS_Y)
    VisualizationService.draw_main_menu(GlobalState.SCREEN, GlobalState.PRESS_Y)


def gameplay_phase():
    """Render the gameplay of the game."""
    events = pygame.event.get()
    
    for event in events:
        if is_close_app_event(event):
            GlobalState.GAME_STATE = GameStatus.GAME_END
            return

        # If the player presses the key, the dialog will be displayed
        if event.type == pygame.KEYDOWN:
            if Dialog.typing:
                Dialog.typing = False
                Dialog.rendering_text = Dialog.get_current_messages()[Dialog.message_index]
                Dialog.full_text_displayed = True
            elif Dialog.message_index < len(Dialog.get_current_messages()) - 1:
                Dialog.message_index += 1
                Dialog.start_typing()
            else:
                Dialog.active = False
                # Check if the lights are on and the last message has been displayed
                if button.lights and Dialog.use_light_messages and Dialog.message_index == len(Dialog.messages_lights) - 1:
                    GlobalState.GAME_STATE = GameStatus.END_BACKGROUND
                    return
                
        button.handle_event(event) # Update the button event

    # Background rendering
    GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL)
    VisualizationService.draw_gameplay_background_with_scroll(GlobalState.SCREEN, GlobalState.SCROLL, button)
    
    # Draw the button
    button.draw(GlobalState.SCREEN)
    
    # Update button logic if the button is pressed
    button.update_lights()

    # Switch to the light-based messages when the lights are on
    if button.lights and not Dialog.use_light_messages:
        Dialog.use_light_messages = True
        Dialog.message_index = 0
        Dialog.start_typing()
    
    # Initialize the dialog
    if not Dialog.active:
        Dialog.active = True
        Dialog.start_typing()

    # Display the first messages and the others gradually
    if Dialog.active:
        Dialog.draw_dialogue_box(GlobalState.SCREEN, 40, 50, 720, 200) 
        Dialog.draw_message(GlobalState.SCREEN, VisualizationService.get_main_font(), 80, 80, 650, 45)


def end_background_phase():
    """Render the final ending background."""
    events = pygame.event.get()

    for event in events:
        if is_close_app_event(event):
            GlobalState.GAME_STATE = GameStatus.GAME_END
            return
        
        # Allow exiting or restarting from the end phase
        if event.type == pygame.KEYDOWN:
            GlobalState.GAME_STATE = GameStatus.GAME_END
            return

    # Background rendering
    GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL)
    VisualizationService.draw_end_background(GlobalState.SCREEN, GlobalState.SCROLL)


def exit_game_phase():
    """Render the exit game phase."""
    pygame.quit()
    sys.exit()