import tkinter
import tkinter.filedialog
import os
from player import Player

"""
TODO:
    [] Adicionar funcionalidades de aumentar / diminuir o volume da música
    [] Configurar o nome atual da música para atualizar automaticamente quando mudamos de música
    [] Personalizar melhor os botões (talvez usar imagens caso possível - Buscar images grátis)
"""

class MusicPlayer(tkinter.Frame):
    def __init__(self, master = None):
        # Configurações do layout da janela
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.player = Player()
        self.configure_gui()

    def configure_gui(self):
        self.master.title("Music Player")
        self.master.geometry("300x300")
        self.master.resizable(False, False)
        self.create_buttons()

    def create_buttons(self):
        self.select_music_button()
        self.select_playlist_button()
        self.previous_music_button()
        self.play_music_button()
        self.next_music_button()

    def select_music_button(self):
        select_music_bttn = tkinter.Button(self.master, text = "Select music", command = self.player.select_music)
        select_music_bttn.pack(side = tkinter.constants.TOP, anchor = tkinter.constants.NE)

    def select_playlist_button(self):
        playlist_select_btn = tkinter.Button(self.master, text="Open a playlist", fg="blue", command=self.player.ask_for_playlist_path)
        playlist_select_btn.pack(side = tkinter.constants.TOP, anchor = tkinter.constants.NW)

    def play_music_button(self):
        play_music_bttn = tkinter.Button(self.master, text="Play / Pause", command=self.player.play_and_pause_music)
        play_music_bttn.place(relx=0.5, rely=0.5, anchor=tkinter.constants.CENTER)

    def next_music_button(self):
        next_music_btton = tkinter.Button(self.master, text="Next", command=self.player.next_music)
        next_music_btton.pack(side = tkinter.constants.RIGHT)

    def previous_music_button(self):
        previous_music_btton = tkinter.Button(self.master, text="Previous", command=self.player.previous_music)
        previous_music_btton.pack(side = tkinter.constants.LEFT)

if __name__ == "__main__":
    root = tkinter.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
