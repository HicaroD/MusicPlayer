from shutil import ExecError
import tkinter
import tkinter.constants
from typing import Type
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
	[] Adicionar funcionalidades para pausar, voltar a tocar, ir para próxima música e etc
"""

class MusicPlayer(object):
	def __init__(self):
		self.window = tkinter.Tk()
		self.window.title("MusicPlayer")
		self.window.geometry("720x480")
		self.window.configure(bg="black")

		self.home_path = os.path.expanduser("~")
		self.current_playlist_path = self.get_playlist_path()

	def play_music(self):
		if(self.current_playlist_path != None):
			for music in self.get_musics_in_folder():
				music_path = os.path.join(self.current_playlist_path, music)

				player = vlc.MediaPlayer(music_path)		
				player.play()

	def get_musics_in_folder(self):
		try:
			if(self.current_playlist_path != None):
				musics = [music for music in os.listdir(self.current_playlist_path) if music.endswith(".mp3")]
				return musics

		except TypeError as e: 
			print(f"Select an playlist and make sure it has audio files. Code error --> {e}")
			sys.exit()

		except Exception as e: 
			print(f"ERROR --> {e}")

	
	def get_playlist_path(self):
		return tkinter.filedialog.askdirectory()

	def select_playlist_button(self): 
		btn = tkinter.Button(self.window, text="Open a playlist", fg="blue", command=self.get_playlist_path)

		# Place button in the top-left corner
		btn.pack(side = tkinter.constants.TOP, anchor = tkinter.constants.NW)
		
	def run(self): 
		self.play_music()
		self.window.mainloop()

if __name__ == "__main__": 
	mainWindow = MusicPlayer().run()