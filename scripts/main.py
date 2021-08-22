import tkinter
import tkinter.constants
import vlc
import os
import tkinter.filedialog 
import sys

"""
TODO: 
    [X] Obter os árquivos de aúdio na pasta
    [X] Tocar áudio
    [X] Criar botão para escolher a playlist
    [X] Fazer o player iterar sobre a lista de músicas
    [X] Botão para tocar música
    [X] Botão para pausar
    [X] Botão para próxima música
    [X] Botão para voltar para música anterior
    [] Mostrar o nome da atual música que está tocando no centro da tela
    [] Personalizar melhor os botões (talvez usar imagens caso possível)
"""


class MusicPlayer(object):
    def __init__(self):
        # Configurações do layout da janela
        self.window = tkinter.Tk()
        self.window.title("Music Player")
        self.window.geometry("480x480")

        # Setup padrão para o MusicPlayer funcionar
        self.draw_buttons()
        self.current_playlist_path = self.ask_for_playlist_path()
        self.Player = vlc.Instance("--loop")
        self.playerList = self.create_playlist()
        self.window.mainloop()

    def ask_for_playlist_path(self):
        return tkinter.filedialog.askdirectory()

    def get_musics_in_folder(self):
        return [os.path.join(self.current_playlist_path, music) for music in os.listdir(self.current_playlist_path) if music.endswith(".mp3")]

    def create_playlist(self):
        playlist = self.Player.media_list_new() # Criar playlist vazia

        for music in self.get_musics_in_folder():
            print(f"Fetching {music} from {self.current_playlist_path}")
            playlist.add_media(self.Player.media_new(music)) 

        playerList = self.Player.media_list_player_new() # Criar um tocador 
        playerList.set_media_list(playlist) # Adicionando playlist ao tocador 

        return playerList

    def play_music(self):
        print("Playing music")
        self.playerList.play()
        
    def pause_music(self):
        print("Pausing music")
        self.playerList.pause()

    def next_music(self):
        print("Next music")
        self.playerList.next()

    def previous_music(self):
        print("Previous music")
        self.playerList.previous()

    def draw_buttons(self):
        self.select_playlist_button()
        self.previous_music_button()
        self.pause_music_button()
        self.play_music_button()
        self.next_music_button()
    
    def select_playlist_button(self): 
        btn = tkinter.Button(self.window, text="Open a playlist", fg="blue", command=tkinter.filedialog.askdirectory)
        btn.pack(side = tkinter.constants.TOP, anchor = tkinter.constants.NW)

    def play_music_button(self):
        play_music_bttn = tkinter.Button(self.window, text="Play", command=self.play_music)
        play_music_bttn.pack(side=tkinter.constants.BOTTOM, anchor=tkinter.constants.S)

    def pause_music_button(self):   
        pause_bttn = tkinter.Button(self.window, text="Pause", command=self.pause_music)
        pause_bttn.pack(side=tkinter.constants.BOTTOM, anchor=tkinter.constants.S)

    def next_music_button(self):
        next_music_btton = tkinter.Button(self.window, text="Next", command=self.next_music)
        next_music_btton.pack(side=tkinter.constants.RIGHT, anchor=tkinter.constants.SE)

    def previous_music_button(self):
        previous_music_btton = tkinter.Button(self.window, text="Previous", command=self.previous_music)
        previous_music_btton.pack(side=tkinter.constants.BOTTOM, anchor=tkinter.constants.SW)
        

if __name__ == "__main__": 
    mainWindow = MusicPlayer()
