import tkinter
import tkinter.filedialog
import os
from player import Player

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
        self.player = Player()
        self.configure_gui()

    def configure_gui(self):
        self.master.title("Music Player")
        self.master.geometry("400x400")
        self.master.resizable(False, False)
        self.draw_buttons()

    def draw_buttons(self):
        self.select_music_button()
        self.select_playlist_button()
        self.previous_music_button()
        self.play_music_button()
        self.next_music_button()

    def select_music_button(self):
        select_music_bttn = Button.make_button(self.master, "Select music", self.player.select_music)
        select_music_bttn.pack(side = tkinter.constants.TOP, anchor = tkinter.constants.CENTER)

    def select_playlist_button(self):
        playlist_select_btn = Button.make_button(self.master, "Open playlist", self.player.ask_for_playlist_path)
        playlist_select_btn.pack(side = tkinter.constants.TOP, anchor = tkinter.constants.CENTER)

    def play_music_button(self):
        play_music_bttn = Button.make_button(self.master, "Play/Pause", self.player.play_and_pause_music)
        play_music_bttn.place(relx=0.5, rely=0.5, anchor=tkinter.constants.CENTER)

    def next_music_button(self):
        next_music_btton = Button.make_button(self.master, "Next", self.player.next_music)
        next_music_btton.pack(side = tkinter.constants.RIGHT)

    def previous_music_button(self):
        previous_music_button = Button.make_button(self.master, "Previous", self.player.previous_music)
        previous_music_button.pack(side = tkinter.constants.LEFT)

class Button:
    # ps.: It's not part of tkinter.Button() class
    @staticmethod
    def make_button(master, text, target):
        return tkinter.Button(master, text = text, command = target)

if __name__ == "__main__":
    root = tkinter.Tk()
    music_player = Application(root)
    root.mainloop()
