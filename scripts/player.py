import tkinter
import tkinter.messagebox
import vlc
import os

vlc_instance = vlc.Instance("--loop")

class PlaylistManager:
    def get_songs_in_folder(self, folder_path):
        try:
            print(f"Fetching musics from folder: {folder_path}")
            songs = [os.path.join(folder_path, music) for music in os.listdir(folder_path) if music.endswith(".mp3")]

            if not songs:
                raise FileNotFoundError

            return songs

        except (TypeError, FileNotFoundError) as e:
            print(e)
            tkinter.messagebox.showwarning(title= "Incompatible playlist",
                                           message="Insert a playlist or a valid playlist (which is a folder with .mp3 files)")
            return None

    def ask_for_folder_path(self):
        return tkinter.filedialog.askdirectory()

    def create_playlist(self, songs) -> vlc.MediaList:
        if(songs):
            playlist = vlc_instance.media_list_new(songs)
            return playlist


class MusicPlayerCreator:
    """Creates an instance of a Music Player"""
    def __init__(self):
        self.playlist = PlaylistManager()

    def select_music(self) -> vlc.MediaPlayer:
        music_path = tkinter.filedialog.askopenfilename()

        if not music_path.endswith(".mp3"):
            raise ValueError("Select an valid file -> mp3")

        return vlc.MediaPlayer(music_path), music_path

    def create_player(self):
       self.current_folder_path = self.playlist.ask_for_folder_path()
       print(f"current_folder_path: {self.current_folder_path}")

       player = vlc_instance.media_list_player_new()

       if(type(self.current_folder_path) is str and len(self.current_folder_path) > 0):
           songs = self.playlist.get_songs_in_folder(self.current_folder_path)
           playlist = self.playlist.create_playlist(songs)
           player.set_media_list(playlist)
           return player
       return player # Returns an empty player 


class MusicPlayer():
    def __init__(self):
        self.configure_mp3_player()

    def configure_mp3_player(self) -> None:
        self.player = MusicPlayerCreator()
        self.music_player = None

    def is_anything_playing(self):
        if(self.music_player is not None):
            return self.music_player.is_playing()

    def create_player(self) -> None:
        """Creates an MusicPlayer using an entire folder with .mp3 files"""
        self.music_player = self.player.create_player()

    def select_music(self) -> None:
        """Selects an individual music"""
        if(self.is_anything_playing()):
            self.music_player.stop()

        self.music_player, music_path = self.player.select_music()
        print(f"Selecting music: {music_path}")

    def play_and_pause_music(self) -> None:
        if(self.is_anything_playing()):
            self.music_player.pause()
        else:
            self.music_player.play()

    def next_music(self) -> None:
        self.music_player.next()

    def previous_music(self) -> None:
        self.music_player.previous()
