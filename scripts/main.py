import tkinter
import tkinter.filedialog
import os
from player import MusicPlayer

"""
TODO:
    [] Pensar em maneiras melhores de gerenciar a criação de botões, existe muito código repetido
       de manter e extender caso eu queira adicionar novos botões
    [] Adicionar funcionalidades de aumentar / diminuir o volume da música
    [] Configurar o nome atual da música para atualizar automaticamente quando mudamos de música
    [] Personalizar melhor os botões (talvez usar imagens caso possível - Buscar images grátis)
"""

class Application(tkinter.Frame):
    def __init__(self, master = None):
        # Configurações do layout da janela
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.player = MusicPlayer()
        self.configure_gui()

    def configure_gui(self):
        self.master.title("Music Player")
        self.master.geometry("300x300")
        self.master.resizable(False, False)
        self.draw_buttons()

    def draw_buttons(self):
        self.select_music_button()
        self.select_playlist_button()
        self.previous_music_button()
        self.play_music_button()
        self.next_music_button()

    def make_button(self, text, target):
        return tkinter.Button(self.master, text = text, command = target)

    def select_music_button(self):
        select_music_bttn = self.make_button("Select music", self.player.select_music)
        select_music_bttn.pack(side = tkinter.constants.TOP, anchor = tkinter.constants.CENTER)

    def select_playlist_button(self):
        playlist_select_btn = self.make_button("Open playlist", self.player.ask_for_playlist_path)
        playlist_select_btn.pack(side = tkinter.constants.TOP, anchor = tkinter.constants.CENTER)

    def play_music_button(self):
        play_music_bttn = self.make_button("Play / Pause", self.player.play_and_pause_music)
        play_music_bttn.place(relx=0.5, rely=0.5, anchor=tkinter.constants.CENTER)

    def next_music_button(self):
        next_music_btton = self.make_button("Next", self.player.next_music)
        next_music_btton.pack(side = tkinter.constants.RIGHT)

    def previous_music_button(self):
        previous_music_btton = self.make_button("Previous", self.player.previous_music)
=======
        select_music_bttn = self.make_button(text = "Select music", target = self.player.select_music)
        select_music_bttn.pack(side = tkinter.constants.TOP, anchor = tkinter.constants.NE)

    def select_playlist_button(self):
        playlist_select_btn = self.make_button(text = "Select playlist", target = self.player.ask_for_playlist_path)
        playlist_select_btn.pack(side = tkinter.constants.TOP, anchor = tkinter.constants.NE)

    def play_music_button(self):
        play_music_bttn = self.make_button(text = "Play / Pause", target = self.player.play_and_pause_music)
        play_music_bttn.place(relx=0.5, rely=0.5, anchor=tkinter.constants.CENTER)

    def next_music_button(self):
        next_music_btton = self.make_button(text = "Next", target = self.player.next_music)
        next_music_btton.pack(side = tkinter.constants.RIGHT)

    def previous_music_button(self):
        previous_music_btton = self.make_button(text = "Previous", target = self.player.previous_music)
>>>>>>> a290601542af2b9223ddcc9b2ed4fa7a04387e12
        previous_music_btton.pack(side = tkinter.constants.LEFT)

if __name__ == "__main__":
    root = tkinter.Tk()
    music_player = Application(root)
    root.mainloop()
