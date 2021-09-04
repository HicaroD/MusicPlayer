import tkinter
import tkinter.filedialog
import os
import vlc

"""
TODO:
    [] Configurar o nome atual da música para atualizar automaticamente quando mudamos de música
    [] Personalizar melhor os botões (talvez usar imagens caso possível - Buscar images grátis)
    [] Adicionar funcionalidades de aumentar / diminuir o volume da música
"""

class MusicPlayer(tkinter.Frame):
    def __init__(self, master = None):
        # Configurações do layout da janela
        tkinter.Frame.__init__(self, master)
        self.master = master
        self.configure_gui()
        self.configure_mp3_player()

    def configure_gui(self):
        self.master.title("Music Player")
        self.master.geometry("300x300")
        self.master.resizable(False, False)
        self.create_buttons()

    def configure_mp3_player(self):
        self.player_instance = vlc.Instance("--loop")
        self.music_player = None
        self.current_music_name = self.get_current_music_name()

    def create_buttons(self):
        self.select_music_button()
        self.select_playlist_button()
        self.previous_music_button()
        self.play_music_button()
        self.next_music_button()

    def select_music(self):
        music_path = tkinter.filedialog.askopenfilename()
        if not music_path.endswith(".mp3"):
            raise Exception("Select an valid file -> mp3")

        if(self.music_player is not None and self.music_player.is_playing()):
            self.music_player.stop()
        print(f"Fetching {music_path} to music player")
        self.music_player = vlc.MediaPlayer(music_path)

    def create_music_label(self):
        self.current_music_label = tkinter.Label(self.master, text = self.get_current_music_name())
        self.current_music_label.place(relx=0.5, rely=0.6, anchor = tkinter.constants.CENTER)

    def ask_for_playlist_path(self):
        # Ask for a new playlist to play
        self.current_playlist_path = tkinter.filedialog.askdirectory()

        if(self.music_player is not None and self.music_player.is_playing()):
            self.music_player.stop()

        print(f"Changing playlist to {self.current_playlist_path}")
        self.music_player = self.create_playlist_player()

    def get_songs_in_folder(self):
        try:
            return [os.path.join(self.current_playlist_path, music) for music in os.listdir(self.current_playlist_path) if music.endswith(".mp3")]

        except (TypeError, FileNotFoundError) as e:
            print("Insert a playlist or a valid playlist (which is a folder with .mp3 files)")
            print(f"Error code -> {e}")
            return None

    def get_current_music_name(self):
        if(self.music_player is not None and self.music_player.is_playing()):
            music_name = self.music_player.get_media_player().get_media().get_mrl()
            print("get_current_music_name() -->" + music_name)
            # Find the last occurence of '/' and get the rest of the string, it's gonna be the name of the music
            return music_name[music_name.rindex('/'):]

    def create_playlist_player(self):
        self.songs = self.get_songs_in_folder()
        if(self.songs):
            self.playlist = self.player_instance.media_list_new(self.get_songs_in_folder()) # Criar playlist a partir da pasta
            playerList = self.player_instance.media_list_player_new() # Criar um tocador 
            playerList.set_media_list(self.playlist) # Adicionando playlist ao tocador 
            print(f"Fetching {self.songs} playlist and adding to the playlist player")
            return playerList

    def play_and_pause_music(self):
        if(self.music_player.is_playing()):
            print("Pausing music")
            self.music_player.pause()
        else:
            print("Playing music")
            self.music_player.play()

    def next_music(self):
        print("Next music")
        self.music_player.next()

    def previous_music(self):
        print("Previous music")
        self.music_player.previous()

    def select_music_button(self):
        select_music_bttn = tkinter.Button(self.master, text = "Select music", command = self.select_music)
        select_music_bttn.pack(side = tkinter.constants.TOP, anchor = tkinter.constants.NE)

    def select_playlist_button(self):
        playlist_select_btn = tkinter.Button(self.master, text="Open a playlist", fg="blue", command=self.ask_for_playlist_path)
        playlist_select_btn.pack(side = tkinter.constants.TOP, anchor = tkinter.constants.NW)

    def play_music_button(self):
        play_music_bttn = tkinter.Button(self.master, text="Play / Pause", command=self.play_and_pause_music)
        play_music_bttn.place(relx=0.5, rely=0.5, anchor=tkinter.constants.CENTER)

    def next_music_button(self):
        next_music_btton = tkinter.Button(self.master, text="Next", command=self.next_music)
        next_music_btton.pack(side = tkinter.constants.RIGHT)

    def previous_music_button(self):
        previous_music_btton = tkinter.Button(self.master, text="Previous", command=self.previous_music)
        previous_music_btton.pack(side = tkinter.constants.LEFT)


if __name__ == "__main__":
    root = tkinter.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
