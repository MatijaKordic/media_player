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

# background = #254117 (Dark Forest Green)
# COLOUR_PRIMARY = "#2e3f4f"
# COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#848482"
# COLOUR_LIGHT_TEXT = "#eee"
# COLOUR_DARK_TEXT = "#8095a8"

class Player(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style(self)
        # style.theme_use("clam")

        style.configure("TFrame", background=COLOUR_LIGHT_BACKGROUND)
        style.configure("Background.TFrame", background=COLOUR_LIGHT_BACKGROUND)
        # style.configure("PomodoroButton.TButton", 
        #                 background=COLOUR_SECONDARY,
        #                 foreground=COLOUR_LIGHT_TEXT
        #                 )
        # style.map("PomodoroButton.TButton", 
        #                 background=[("active", COLOUR_PRIMARY), ("disabled", COLOUR_LIGHT_TEXT)]
        #                 )

        # # our class is a tk object and not a ttk object
        # # this means that we can't set style on self directly
        # # so we need to set it this way
        self["background"] = COLOUR_LIGHT_BACKGROUND

        self.geometry("450x850")
        self.minsize(200, 100)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        width = 25
        height = 25
        play_img = Image.open("/Users/matija/Desktop/Projects/media_player/assets/play.png").resize((width,height), Image.ANTIALIAS)
        self.play_img =  ImageTk.PhotoImage(play_img)
        pause_img = Image.open("/Users/matija/Desktop/Projects/media_player/assets/pause.png").resize((width,height), Image.ANTIALIAS)
        self.pause_img =  ImageTk.PhotoImage(pause_img)
        stop_img = Image.open("/Users/matija/Desktop/Projects/media_player/assets/stop.png").resize((width,height), Image.ANTIALIAS)
        self.stop_img =  ImageTk.PhotoImage(stop_img)
        shuffle_img = Image.open("/Users/matija/Desktop/Projects/media_player/assets/shuffle.png").resize((width,height), Image.ANTIALIAS)
        self.shuffle_img =  ImageTk.PhotoImage(shuffle_img)
        repeat_img = Image.open("/Users/matija/Desktop/Projects/media_player/assets/repeat.png").resize((width,height), Image.ANTIALIAS)
        self.repeat_img =  ImageTk.PhotoImage(repeat_img)
        next_img = Image.open("/Users/matija/Desktop/Projects/media_player/assets/forward.png").resize((width,height), Image.ANTIALIAS)
        self.next_img =  ImageTk.PhotoImage(next_img)
        back_img = Image.open("/Users/matija/Desktop/Projects/media_player/assets/backward.png").resize((width,height), Image.ANTIALIAS)
        self.back_img =  ImageTk.PhotoImage(back_img)
        vup_img = Image.open("/Users/matija/Desktop/Projects/media_player/assets/volume_up.png").resize((width,height), Image.ANTIALIAS)
        self.vup_img =  ImageTk.PhotoImage(vup_img)
        vdown_img = Image.open("/Users/matija/Desktop/Projects/media_player/assets/volume_down.png").resize((width,height), Image.ANTIALIAS)
        self.vdown_img =  ImageTk.PhotoImage(vdown_img)

        # Initiating Pygame
        pygame.mixer.init()
        self.state = 'OFF'
        self.song_length = 0
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = tk.StringVar()
        # Declaring Status Variable
        self.status = tk.StringVar()

        # menu_container = ttk.Frame(self, width=450, height=10)
        # menu_container.grid(row=0, column=0, sticky="W")
        # menu_container.columnconfigure(0, weight=1)
        # menu_container.rowconfigure(0, weight=1)

        button_container = ttk.Frame(self, width=450, height=100, padding=10)
        button_container.grid(row=0, column=0, columnspan=2, sticky="NEW")
        button_container.columnconfigure((0, 1, 2, 3, 4), weight=1)
        button_container.rowconfigure(0, weight=1)

        next_song = tk.Button(button_container, image=self.next_img, borderwidth=0, bg=COLOUR_LIGHT_BACKGROUND, command=self.next)
        prev_song = tk.Button(button_container, image=self.back_img, width=25, borderwidth=0, command=self.back)
        volume_up = tk.Button(button_container, image=self.vup_img, width=25, borderwidth=0, command=self.increase_volume)
        volume_down = tk.Button(button_container, image=self.vdown_img, width=25, borderwidth=0, command=self.decrease_volume)
        # add = tk.Button(button_container, text="Add", borderwidth=0, command=self.open)

        next_song.grid(row=0, column=4)
        prev_song.grid(row=0, column=0)
        volume_up.grid(row=1, column=3)
        volume_down.grid(row=1, column=1)
        # add.grid(row=1, column=0)

        play = tk.Button(button_container,command=self.play, image=self.play_img, width=25, borderwidth=0)
        stop = tk.Button(button_container, command=self.stop, image=self.stop_img, width=25, borderwidth=0)
        replay = tk.Button(button_container, text="Replay", image=self.repeat_img, width=25, borderwidth=0, command=self.replay)
        shuffle = tk.Button(button_container, image=self.shuffle_img, width=25, borderwidth=0)
        pause = tk.Button(button_container, command=self.pause, image=self.pause_img, width=25, borderwidth=0)
        play.grid(row=0, column=2)
        stop.grid(row=0, column=3)
        replay.grid(row=1, column=4)
        # shuffle.grid(row=1, column=5)
        pause.grid(row=0, column=1)

        self.variable = tk.StringVar(value="Add Music")
        self.value = ["Add file", "Add folder"]
        my_menu = tk.OptionMenu(button_container, self.variable, *self.value, command=self.add_folder)
        self.config(menu=my_menu)
        my_menu.grid(row=1, column=0)

        # add_song_menu = tk.OptionMenu(my_menu, self.variable, *self.value, command=self.add_folder)
        # add_song_menu.grid(row=1, column=0)

        # create Status bar
        self.status_bar = ttk.Label(button_container, text="", relief="groove")
        self.status_bar.grid(row=2, columnspan=5, sticky="EW", ipady=10)

        self.song_slider = ttk.Scale(button_container, from_=0, to=100, orient="horizontal", value=0, command=self.slide)
        self.song_slider.grid(row=3, columnspan=5, sticky="EW", ipady=10)

        # volume slider
        self.volume_slider = ttk.Scale(button_container, from_=0, to=1, orient="horizontal", value=1, command=self.volume, length=50)
        self.volume_slider.grid(row=1, column=2, sticky="EW", ipady=10)

        # # temp slide label
        # self.slider_label = tk.Label(button_container, text="0")
        # self.slider_label.grid(row=4, columnspan=5, ipady=10, sticky="EW")

        other_container = ttk.Frame(self, width=450, height=300, padding=10)
        other_container.grid(row=1, column=0, sticky="NESW")
        other_container.columnconfigure(0, weight=1)
        other_container.rowconfigure(0, weight=1)

        self.items_dict = dict()
        self.items = []
        self.list_items = tk.StringVar(value=self.items)
        self.playlist = tk.Listbox(other_container, listvariable=self.list_items, selectmode='SINGLE', relief='groove')
        self.playlist.grid(row=0, column=0, sticky="NESW")
        self.playlist.bind("<Double-Button-1>", self.play)

        # link a scrollbar to a list
        scrollbar = ttk.Scrollbar(
            other_container,
            orient='vertical',
            command=self.playlist.yview
            )

        self.playlist['yscrollcommand'] = scrollbar.set

        scrollbar.grid(
            column=1,
            row=0,
            sticky='ns'
            )
    
    # Grab song length time
    def song_data(self):
        if self.state == 'Paused':
            return
        current_time = pygame.mixer.music.get_pos() / 1000

        # throw up temp lable to get data
        # self.slider_label.config(text=f'Slider: {int(self.song_slider.get())} and Song Position: {int(current_time)}')
        converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

        current_song = self.playlist.curselection()
        current_song = self.playlist.get(current_song)
        song_path = os.getcwd()
        current_song = f'{song_path}/{current_song}'
        
        # get song length with Mutagen
        song_mutagen = MP3(current_song)
        self.song_length = song_mutagen.info.length
        converted_song_length = time.strftime('%M:%S', time.gmtime(self.song_length))
        
        if int(self.song_slider.get()) == int(self.song_length):
            self.status_bar.config(text=f"Time Elapsed: {converted_song_length}/ {converted_song_length} ")
        elif self.state == 'Paused':
            pass
        elif int(self.song_slider.get()) == int(current_time):
            print("Slider hasn't moved.")
            slider_position = int(self.song_length)
            self.song_slider.config(to=slider_position, value=int(current_time))
        else:
            slider_position = int(self.song_length)
            self.song_slider.config(to=slider_position, value=int(self.song_slider.get()))

            converted_current_time = time.strftime('%M:%S', time.gmtime(int(self.song_slider.get())))
            
            self.status_bar.config(text=f"Time Elapsed:{converted_current_time}/ {converted_song_length} ")
            # self.song_slider.config(value=int(current_time))

            next_time = int(self.song_slider.get()) + 1
            self.song_slider.config(value=next_time)

        # update time
        self.status_bar.after(1000, self.song_data)

    def play(self, *args):
        print(f"State: {self.state}")
        if self.state == 'Paused':
            print('Correct')
            pygame.mixer.music.unpause()
            self.state = 'ON'
            self.song_data()
        else:
            # Displaying Selected Song title
            # song = self.playlist.get(tk.ACTIVE)
            # song_path = os.getcwd()
            # song = f'{song_path}/{song}'
            self.track.set(self.playlist.get(tk.ACTIVE))
            
            # Displaying Status
            pygame.mixer.music.load(self.playlist.get(tk.ACTIVE))
            # pygame.mixer.music.load(song)
            # self.track.set(self.playlist.get(tk.ACTIVE))
            # # Displaying Status
            self.status.set("-Playing")
            pygame.mixer.music.play()
            self.state = 'ON'
            self.song_data()

        # get current volume
        # current_volume = pygame.mixer.music.get_volume()
        # self.slider_label.config(text=current_volume * 100)
        # slider_position = int(self.song_length)
        # self.song_slider.config(to=slider_position, value=0)
    global stopped
    stopped = False
    def stop(self):
        self.status_bar.config(text='')
        self.song_slider.config(value=0)
        pygame.mixer.music.stop()

        # Clear the status bar
        self.status_bar.config(text='')

        global stopped
        stopped = True

    def pause(self, *args):
        pygame.mixer.music.pause()
        self.state = 'Paused'
        print(f"State: {self.state}")

    def replay(self, *args):
        self.track.set(self.playlist.get(tk.ACTIVE))    
        # Displaying Status
        pygame.mixer.music.load(self.playlist.get(tk.ACTIVE))
        # pygame.mixer.music.load(song)
        # self.track.set(self.playlist.get(tk.ACTIVE))
        # # Displaying Status
        self.status.set("-Playing")
        pygame.mixer.music.play(loops=-1)
        self.state = 'ON'
        self.song_data()


    def next(self):
        self.status_bar.config(text='')
        self.song_slider.config(value=0)
        next_track = self.playlist.curselection()
        next_track = next_track[0]+1
        # Displaying Selected Song title
        song = self.playlist.get(next_track)
        song_path = os.getcwd()
        next_track_final = f'{song_path}/{song}'
        END = len(self.items)
        # self.track.set(self.playlist.get(tk.ACTIVE))
        # # Displaying Status
        # self.status.set("-Playing")
        pygame.mixer.music.load(next_track_final)
        pygame.mixer.music.play(loops=0)
        # self.var.set(self.playlist.get(tk.ACTIVE))
        self.playlist.selection_clear(0, END)
        self.playlist.activate(next_track)
        self.playlist.selection_set(next_track, last=None)
        self.state = 'ON'

    def back(self):
        self.status_bar.config(text='')
        self.song_slider.config(value=0)
        previous_track = self.playlist.curselection()
        previous_track = previous_track[0]-1
        # Displaying Selected Song title
        song = self.playlist.get(previous_track)
        song_path = os.getcwd()
        previous_track_final = f'{song_path}/{song}'
        END = len(self.items)
        # self.track.set(self.playlist.get(tk.ACTIVE))
        # # Displaying Status
        # self.status.set("-Playing")
        pygame.mixer.music.load(previous_track_final)
        pygame.mixer.music.play(loops=0)
        # self.var.set(self.playlist.get(tk.ACTIVE))
        self.playlist.selection_clear(0, END)
        self.playlist.activate(previous_track)
        self.playlist.selection_set(previous_track, last=None)
        self.state = 'ON'

    def slide(self, *args):
        # converted_song_length = time.strftime('%M:%S', time.gmtime(self.song_length))
        # self.slider_label.config(text=f'{int(self.song_slider.get())} of {converted_song_length}')
        song = self.playlist.get(tk.ACTIVE)
        song_path = os.getcwd()
        song = f'{song_path}/{song}'
        # self.track.set(self.playlist.get(tk.ACTIVE))
        # Displaying Status
        # pygame.mixer.music.load(self.playlist.get(tk.ACTIVE))
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0, start=int(self.song_slider.get()))

    def add_file(self, *args):
        directory = askopenfilename()
        # p = re.compile(r'(.*\/)(.+)(\.mp3)')
        # # reg = r'.*\/(.+\.mp3)'
        # x = p.search(directory)
        # directory = directory.replace(x.group(1), '')
        # directory = directory.replace(x.group(3), '')
        song_name = directory.split('/')[-1].split('.')[0]
        self.items.append(directory)
        self.list_items.set(value=self.items)
        # self.play()
        self.items_dict["song_name"] = directory

        # if x:
        #     self.items.append(x.group(2))
        #     self.list_items.set(value=self.items)    
        # # Inserting Songs into Playlist
        # else:
        #     self.items.append(directory)
        #     self.list_items.set(value=self.items)

    def add_folder(self, *args):
        if self.variable.get() == "Add file":
            self.add_file()
        else:
            directory = askdirectory()
            os.chdir(directory)
            songtracks = os.listdir()
            # Inserting Songs into Playlist
            for track in songtracks:
                print(track)
                if sndhdr.what(track) or track.endswith(".mp3"):
                    print("Audio")
                    self.items.append(track)
                else:
                    print("Not audio!")
            self.list_items.set(value=self.items)
            # os.chdir(directory)
            # song_list = os.listdir()

    def open(self):  
        top = tk.Toplevel(self)
        add_file = ttk.Button(top, text="Add file", command=self.add_file)
        add_folder = ttk.Button(top, text="Add folder", command=self.add_folder)
        add_file.grid(row=0, column=0)
        add_folder.grid(row=0, column=1)

    def increase_volume(self):
        pass

    def decrease_volume(self):
        pass

    def volume(self, *args):
        pygame.mixer.music.set_volume(self.volume_slider.get())

        # get current volume
        # current_volume = pygame.mixer.music.get_volume()
        # self.slider_label.config(text=current_volume * 100)

    def delete_song(self):
        self.stop()
        self.playlist.delete(ANCHOR)

        pygame.mixer.music.stop()

    def delete_all_songs(self):
        self.stop()
        self.playlist.delete(0, END)

        pygame.mixer.music.stop()

# root = tk.Tk()
root = Player()


root.mainloop()