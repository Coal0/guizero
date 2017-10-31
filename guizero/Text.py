from tkinter import Label, StringVar
from . import utilities as utils

class Text:

    def __init__(self, master, text="", size=12, color="black", text_color=None, bg=None, font="Helvetica", grid=None, align=None):

        # Description of this object (for friendly error messages)
        self.description = "[Text] object with text \"" + str(text) + "\""

        # Save some of the config
        self.current_size = size
        if text_color is None:          # text_color overrides old color property
            self.current_color = color
        else:
            self.current_color = text_color
        self.bg_color = bg
        self.current_font = font

        self.text = str(text)

        # Create a tk Label object within this object
        self.tk = Label(master, text=text, fg=self.text_color, bg=bg, font=(font, size))

        # Pack this object
        try:
            utils.auto_pack(self, master, grid, align)
       	except AttributeError:
            utils.error_format( self.description + "\n" +
            "Could not add to interface - check first argument is [App] or [Box]")

    # PROPERTIES
    # ----------------------------------

    # The text value
    @property
    def value(self):
        return (self.text)

    @value.setter
    def value(self, value):
        self.tk.config(text=value)
        self.text = str(value)
        self.description = "[Text] object with text \"" + str(value) + "\""

    # The text color
    @property
    def text_color(self):
        return (self.current_color)

    @text_color.setter
    def text_color(self, color):
        self.tk.config(fg=color)
        self.current_color = color

    # The background color
    @property
    def bg(self):
        return (self.bg_color)

    @bg.setter
    def bg(self, color):
        self.tk.config(bg=color)
        self.bg_color = color

    # The font face
    @property
    def font(self):
        return (self.current_font)

    @font.setter
    def font(self, font):
        self.current_font = font
        self.tk.config(font=(self.current_font, self.current_size))

    # The font size
    @property
    def size(self):
        return (self.current_size)

    @size.setter
    def size(self, size):
        self.current_size = size
        self.tk.config(font=(self.current_font, self.current_size))

    # METHODS
    # -------------------------------------------

    # Clear text (set to empty string)
    def clear(self):
        self.text = ""
        self.tk.config(text="")

    # Append some text onto the end of the existing text
    def append(self, text):
        new_text = self.text + str(text)
        self.text = new_text
        self.tk.config(text=new_text)
        self.description = "[Text] object with text \"" + new_text + "\""


    # DEPRECATED METHODS
    # --------------------------------------------

    # Sets the text colour
    def color(self, color):
        self.current_color = color
        self.tk.config(fg=color)
        utils.deprecated("Text color() is deprecated. Please use the text_color property instead.")

    # Set the font
    def font_face(self, font):
        self.current_font = font
        self.tk.config(font=(self.current_font, self.current_size))
        utils.deprecated("Text font_face() is deprecated. Please use font property instead.")

    # Set the font size
    def font_size(self, size):
        self.current_size = size
        self.tk.config(font=(self.current_font, self.current_size))
        utils.deprecated("Text font_size() is deprecated. Please use the size property instead.")

     # Returns the text
    def get(self):
        return self.text
        utils.deprecated("Text get() is deprecated. Please use the value property instead.")

    # Sets the text
    def set(self, text):
        self.text = str(text)
        self.tk.config(text=self.text)
        self.description = "[Text] object with text \"" + str(text) + "\""
        utils.deprecated("Text set() is deprecated. Please use the value property instead.")
