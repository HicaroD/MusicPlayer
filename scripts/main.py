import tkinter
import tkinter.filedialog
import os
from player import MusicPlayer

"""
TODO:
    [] Adicionar funcionalidades de aumentar / diminuir o volume da música
    [] Configurar o nome atual da música para atualizar automaticamente quando mudamos de música
"""


class Button:
    @staticmethod
    def make_button(master, text, target):
        return tkinter.Button(master, text = text, command = target)


class Application(tkinter.Frame):
    def __init__(self, master = None):
        # Configurações do layout da janela
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.player = MusicPlayer()
        self.configure_gui()

    def configure_gui(self) -> None:
        self.master.title("Music Player")
        self.master.geometry("400x400")
        self.master.resizable(False, False)
        self.draw_buttons()

    def draw_buttons(self) -> None:
        self.select_music_button()
        self.select_playlist_button()
        self.previous_music_button()
        self.play_music_button()
        self.next_music_button()

    def select_music_button(self) -> None:
        select_music_bttn = Button.make_button(self.master, "Select music", self.player.select_music)
        select_music_bttn.pack(side = tkinter.constants.TOP, anchor = tkinter.constants.CENTER)

    def select_playlist_button(self) -> None:
        playlist_select_btn = Button.make_button(self.master, "Open playlist", self.player.create_player)
        playlist_select_btn.pack(side = tkinter.constants.TOP, anchor = tkinter.constants.CENTER)

    def play_music_button(self) -> None:
        play_music_bttn = Button.make_button(self.master, "Play/Pause", self.player.play_and_pause_music)
        play_music_bttn.place(relx=0.5, rely=0.5, anchor=tkinter.constants.CENTER)

    def next_music_button(self) -> None:
        next_music_btton = Button.make_button(self.master, "Next", self.player.next_music)
        next_music_btton.pack(side = tkinter.constants.RIGHT)

    def previous_music_button(self) -> None:
        previous_music_button = Button.make_button(self.master, "Previous", self.player.previous_music)
        previous_music_button.pack(side = tkinter.constants.LEFT)


if __name__ == "__main__":
    root = tkinter.Tk()
    music_player = Application(root)
    root.mainloop()
