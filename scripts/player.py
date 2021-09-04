import tkinter
import vlc
import os

class Player(object):
    def __init__(self):
        self.configure_mp3_player()

    def configure_mp3_player(self):
        self.player_instance = vlc.Instance("--loop")
        self.music_player = None
        self.current_music_name = self.get_current_music_name()

    def select_music(self):
        music_path = tkinter.filedialog.askopenfilename()
        if not music_path.endswith(".mp3"):
            raise Exception("Select an valid file -> mp3")

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
