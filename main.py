import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory, askopenfilename
import os
import pygame
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from PIL import Image
from PIL import ImageTk
import sndhdr
from mutagen.mp3 import MP3
import time
import regex as re

# background = "#254117"
# COLOUR_PRIMARY = "#2e3f4f"
# COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#848482"
# COLOUR_LIGHT_TEXT = "#eee"
# COLOUR_DARK_TEXT = "#8095a8"

class Window(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # style = ttk.Style(self)
        # style.theme_use("clam")

        # style.configure("TFrame", background=COLOUR_LIGHT_BACKGROUND)
        # style.configure("Background.TFrame", background=COLOUR_LIGHT_BACKGROUND)

        # self["background"] = COLOUR_LIGHT_BACKGROUND

        # self.geometry("450x850")
        # self.minsize(200, 100)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # container = ttk.Frame(self)
        # container.grid()
        # container.columnconfigure(0, weight=1)

        menu = tk.Menu(root)
        root.config(menu=menu)

        add_song_menu = tk.Menu(menu)
        menu.add_cascade(label="Add Songs", menu=add_song_menu)
        add_song_menu.add_command(label="Add File")


        # self.frames = Player

root = tk.Tk()
app = Window(root)

root.mainloop()
