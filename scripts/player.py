import tkinter
import vlc
import os

class Playlist:
    def __init__(self):
        self.player_instance = vlc.Instance("--loop")

    def get_songs_in_folder(self, folder_path):
        try:
            print(f"Fetching musics from folder: {folder_path}")
            return [os.path.join(folder_path, music) for music in os.listdir(folder_path) if music.endswith(".mp3")]

        except (TypeError, FileNotFoundError) as e:
            print("Insert a playlist or a valid playlist (which is a folder with .mp3 files)")
            print(f"Error code -> {e}")
            return None

    def ask_for_folder_path(self):
        return tkinter.filedialog.askdirectory()

    def create_playlist(self, songs) -> vlc.MediaList:
        if(songs):
            playlist = self.player_instance.media_list_new(songs) # Criando objeto do tipo MediaList (playlist)
            return playlist


class Player:
    def __init__(self):
        self.player_instance = vlc.Instance("--loop")
        self.playlist = Playlist()

    def select_music(self) -> vlc.MediaPlayer:
        music_path = tkinter.filedialog.askopenfilename()

        if not music_path.endswith(".mp3"):
            raise ValueError("Select an valid file -> mp3")

        return vlc.MediaPlayer(music_path)

    def create_player(self) -> vlc.MediaListPlayer:
        try:
            self.current_folder_path = self.playlist.ask_for_folder_path()
            print(f"current_folder_path: {self.current_folder_path}")

            if(type(self.current_folder_path) is not tuple or self.current_folder_path != ""):
                songs = self.playlist.get_songs_in_folder(self.current_folder_path)
                playlist = self.playlist.create_playlist(songs)
                player = self.player_instance.media_list_player_new()
                player.set_media_list(playlist)
                return player
            raise Exception("An error occurs while trying to create a music_player")

        except Exception as e: 
            print(e)


class MusicPlayer():
    def __init__(self):
        self.configure_mp3_player()

    def configure_mp3_player(self) -> None:
        self.player_instance = vlc.Instance("--loop")
        self.player = Player()
        self.music_player = None

    def is_anything_playing(self) -> bool:
        return self.music_player.is_playing()

    def create_player(self) -> None:
        """Creates an MusicPlayer using an entire folder with .mp3 files"""
        self.music_player = self.player.create_player()

    def select_music(self) -> None:
        """Selects an individual music"""
        if(self.is_anything_playing()):
            self.music_player.stop()

        print("Selecting music")
        self.music_player = self.player.select_music()

    def play_and_pause_music(self) -> None:
        if(self.is_anything_playing()):
            self.music_player.pause()
        else:
            self.music_player.play()

    def next_music(self) -> None:
        self.music_player.next()

    def previous_music(self) -> None:
        self.music_player.previous()
