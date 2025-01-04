import pygame

class Dialog:
    """Service to manage the dialog box and messages."""
    message_index = 0 # Track index of the current message being displayed
    # List of predefined messages to display
    messages = [
        "Hey you! I'm Frozty the Snowman! The froztiest of them all! Literally.",
        "I NEED YOUR HELP RIGHT NOW! The tree is missing its lights.",
        "The electrician ditched us for Cancún, so it's DIY time!",
        "What? I'm frozen, so you better do it.",
        "How? OMAIGOSSSH! Your IQ is smaller than a snowball!",
        "There is a HUGE button there Einstein, you might wanna check it out.",
        "Press the button. It's not rocket science; it's button science.",
        "PUSH THE BUTTONNNNNNNNNNN",
        "Okay I'm not gonna shout. Push the button.",
        "Push the GODDAMN button!"
    ]
    # List of predefined messages to display after the lights = True
    messages_lights = [
        "WOHOOO! I knew you were smart ENOUGH!",
        "You have such powerful brain cells, I'm STOKED!",
        "I'm positively glowing... oh wait, that's the tree.",
        "This tree just went from sad to FABULOUS.",
        "Finally, I can brag to the snowfolk about this glorious moment.",
        "I've been wanting a summer vacation to Bali since I was a lil wee kiddo.",
        "I dunno how I never made it so far...",
        "Well, I hope my wishes will come true this year...",
        "Merry xmas and happy new year!"
    ]
    rendering_text = "" # Keeps the text being gradually typed out
    full_text_displayed = False # Flag to indicate if the entire text has been displayed
    typing = False # Flag to indicate if the text is currently being typed
    active = False # Flag to indicate if the dialog box is active
    use_light_messages = False  # Flag to track which set of messages to use

    @staticmethod
    def get_current_messages():
        """Get the appropriate set of messages based on the light state."""
        return Dialog.messages_lights if Dialog.use_light_messages else Dialog.messages

    @staticmethod
    def start_typing():
        """Start typing the current message."""
        current_messages = Dialog.get_current_messages()
        if Dialog.message_index < len(current_messages):
            Dialog.rendering_text = ""
            Dialog.typing = True
            Dialog.full_text_displayed = False

    @staticmethod
    def split_text_into_lines(text, font, max_width):
        """Split text into multiple lines to fit within the given width."""
        words = text.split(" ")
        lines = []
        current_line = "" 

        for word in words:
            test_line = current_line + word + " "
            # Using the font's sixe method to measure the text width
            if font.size(test_line.strip())[0] <= max_width:  
                current_line = test_line
            else:
                lines.append(current_line.strip())
                current_line = word + " "

        if current_line:  # Add any remaining text as the last line
            lines.append(current_line.strip())

        return lines

    @staticmethod
    def gradual_typing(screen, font, full_text, x, y, max_width, line_height):
        """Display text with a gradual typing effect and handle wrapping."""
        if not Dialog.typing:
            return

        # Gradually add characters to the rendering text
        if len(Dialog.rendering_text) < len(full_text):
            Dialog.rendering_text += full_text[len(Dialog.rendering_text)]

        # Split the rendering text into lines
        lines = Dialog.split_text_into_lines(Dialog.rendering_text, font, max_width)

        # Render each line and display it on the screen
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, "Black")
            screen.blit(text_surface, (x, y + i * line_height))

        # If the full text is displayed, stop typing
        if Dialog.rendering_text == full_text:
            Dialog.typing = False
            Dialog.full_text_displayed = True

    @staticmethod
    def draw_message(screen, font, x, y, max_width, line_height):
        """Render the current message gradually or fully based on its status."""
        current_messages = Dialog.get_current_messages()
        if Dialog.message_index < len(current_messages):
            full_text = current_messages[Dialog.message_index]
            if Dialog.full_text_displayed:
                # Split and display full text directly
                lines = Dialog.split_text_into_lines(full_text, font, max_width)
                for i, line in enumerate(lines):
                    text_surface = font.render(line, True, "Black")
                    screen.blit(text_surface, (x, y + i * line_height))
            else:
                # Gradually type the message
                Dialog.gradual_typing(screen, font, full_text, x, y, max_width, line_height)

    @staticmethod
    def draw_dialogue_box(screen, x, y, width, height):
        """Draw the dialogue box."""
        box_color = (0, 0, 255, 60)  # Semi-transparent blue
        border_color = (0, 0, 150)  # Dark border
        textbox_surf = pygame.Surface((width, height), pygame.SRCALPHA)
        textbox_surf.fill(box_color)
        pygame.draw.rect(textbox_surf, border_color, (0, 0, width, height), 6)
        screen.blit(textbox_surf, (x, y))
