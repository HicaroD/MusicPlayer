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
		self.window.title("MusicPlayer")
		self.window.geometry("480x480")

		self.media_player = vlc.Instance("--loop")

	def get_playlist_path(self):
		return tkinter.filedialog.askdirectory()

	def addPlaylist(self):
		# Criando playlist
		self.playlist = self.media_player.media_list_new()

		# Adicionando músicas a playlist
		for music in os.listdir(self.current_playlist_path):
			print("Adding music to playlist: " + music)
			self.playlist.add_media(os.path.join(self.current_playlist_path, music))

		# Setando a playlist 
		self.playlistPlayer = self.media_player.media_list_player_new()
		self.playlistPlayer.set_media_list(self.playlist)

	def play_music(self):
		print("Playing music")
		self.playlistPlayer.play()
		
	def pause_music(self):
		print("Pausing music")
		self.playlistPlayer.pause()

	def next_music(self):
		print("Next music")
		self.playlistPlayer.next()

	def previous_music(self):
		print("Previous music")
		self.playlistPlayer.previous()

	def get_musics_in_folder(self):
		musics = []
		try:
			musics = [music for music in os.listdir(self.current_playlist_path) if music.endswith(".mp3")]
			return musics

		except TypeError as e: 
			print(f"Select an playlist and make sure it has audio files. Code error --> {e}")
			sys.exit()

		except Exception as e: 
			print(f"ERROR --> {e}")

	def drawButtons(self):
		self.select_playlist_button()
		self.previous_music_button()
		self.pause_music_button()
		self.play_music_button()
		self.next_music_button()
	
	def select_playlist_button(self): 
		btn = tkinter.Button(self.window, text="Open a playlist", fg="blue", command=self.get_playlist_path)
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
		
	def run(self): 
		self.drawButtons()
		self.current_playlist_path = self.get_playlist_path()
		self.get_musics_in_folder()
		self.addPlaylist()
		self.window.mainloop()


if __name__ == "__main__": 
	mainWindow = MusicPlayer().run()