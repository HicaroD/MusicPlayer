import tkinter
import tkinter.constants
import vlc
import os
import tkinter.filedialog 

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
    [X] Consertar o botão de mudar playlist (que não afetava em nada na hora que tentava mudar a playlist
    [] Mostrar o nome da atual música que está tocando no centro da tela
    [] Personalizar melhor os botões (talvez usar imagens caso possível)
"""


class MusicPlayer(tkinter.Frame):
    def __init__(self, master = None):
        # Configurações do layout da janela
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.configure_gui()

        # Setup padrão para o MusicPlayer funcionar
        self.create_buttons()
        self.player_instance = vlc.Instance("--loop")
        self.current_playlist_path = tkinter.filedialog.askdirectory()
        self.music_player = self.create_playlist()

    def configure_gui(self):
        self.master.title("Music Player")
        self.master.geometry("480x480")
        self.master.resizable(False, False)

    def ask_for_playlist_path(self):
        # Ask for a new playlist to play
        self.current_playlist_path = tkinter.filedialog.askdirectory()

        if(self.music_player.is_playing()):
            self.music_player.stop()

        print(f"Changing playlist to {self.current_playlist_path}")
        self.music_player = self.create_playlist()

    def get_musics_in_folder(self):
        return [os.path.join(self.current_playlist_path, music) for music in os.listdir(self.current_playlist_path) if music.endswith(".mp3")]

    def create_playlist(self):
        playlist = self.player_instance.media_list_new() # Criar playlist vazia

        for music in self.get_musics_in_folder():
            print(f"Fetching {music} from {self.current_playlist_path}")
            playlist.add_media(self.player_instance.media_new(music)) 

        playerList = self.player_instance.media_list_player_new() # Criar um tocador 
        playerList.set_media_list(playlist) # Adicionando playlist ao tocador 
        return playerList

    def play_music(self):
        print("Playing music")
        self.music_player.play()
        
    def pause_music(self):
        print("Pausing music")
        self.music_player.pause()

    def next_music(self):
        print("Next music")
        self.music_player.next()

    def previous_music(self):
        print("Previous music")
        self.music_player.previous()

    def create_buttons(self):
        self.select_playlist_button()
        self.previous_music_button()
        self.pause_music_button()
        self.play_music_button()
        self.next_music_button()
    
    def select_playlist_button(self): 
        playlist_select_btn = tkinter.Button(self.master, text="Open a playlist", fg="blue", command=self.ask_for_playlist_path)
        playlist_select_btn.grid(column = 0, row = 0)

    def play_music_button(self):
        play_music_bttn = tkinter.Button(self.master, text="Play", command=self.play_music)
        play_music_bttn.grid(column = 1, row = 0)

    def pause_music_button(self):   
        pause_bttn = tkinter.Button(self.master, text="Pause", command=self.pause_music)
        pause_bttn.grid(column = 2, row = 0)
        
    def next_music_button(self):
        next_music_btton = tkinter.Button(self.master, text="Next", command=self.next_music)
        next_music_btton.grid(column = 3, row = 0)

    def previous_music_button(self):
        previous_music_btton = tkinter.Button(self.master, text="Previous", command=self.previous_music)
        previous_music_btton.grid(column = 4, row = 0)
        

if __name__ == "__main__": 
    root = tkinter.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
