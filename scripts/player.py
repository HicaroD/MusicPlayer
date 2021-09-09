import tkinter
import vlc
import os

# TODO: [] Separar a parte de gerenciamento de playlist em outra classe e deixa a classe Player apenas para gerenciar como a música toca.
#          Existe mais de uma responsabilidade nessa classe Player quando deveria ser apenas sobre o tocador e não deveria estar criando botões

class MusicPlayer:
    def __init__(self):
        self.configure_mp3_player()

    def configure_mp3_player(self):
        self.player_instance = vlc.Instance("--loop")
        self.music_player = None

    def select_music(self) -> None:
        music_path = tkinter.filedialog.askopenfilename()

        if not music_path.endswith(".mp3"):
            raise ValueError("Select an valid file -> .mp3")

        if(self.music_player is not None and self.music_player.is_playing()):
            self.music_player.stop()

        print(f"Fetching {music_path} to music player")
        self.music_player = vlc.MediaPlayer(music_path)

    def ask_for_playlist_path(self):
        # Ask for a new playlist to play
        self.current_playlist_path = tkinter.filedialog.askdirectory()

        if(self.music_player is not None and self.music_player.is_playing()):
            self.music_player.stop()

        print(f"Changing playlist to {self.current_playlist_path}")
        self.music_player = self.create_player()

    def get_songs_in_folder(self):
        try:
            playlist_folder = os.listdir(self.current_playlist_path)
            return [os.path.join(self.current_playlist_path, music) for music in playlist_folder if music.endswith(".mp3")]

        except (TypeError, FileNotFoundError) as e:
            print("Insert a playlist or a valid playlist (which is a folder with .mp3 files)")
            print(f"Error code -> {e}")
            return None

    def create_playlist(self):
        self.playlist = self.player_instance.media_list_new(self.get_songs_in_folder()) # Criar playlist a partir da pasta
        return self.playlist

    def create_player(self):
        self.songs = self.get_songs_in_folder()
        if(self.songs):
            self.playlist = self.create_playlist()
            player = self.player_instance.media_list_player_new() # Criar um tocador 
            self.put_songs_in_playlist_player(player)
        return player

    def put_songs_in_playlist_player(self, playlist_player):
            playlist_player.set_media_list(self.playlist) # Adicionando playlist ao tocador 
            print(f"Fetching {self.songs} playlist and adding to the playlist player")

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
