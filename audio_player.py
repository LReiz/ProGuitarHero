import os

MUSICS_PATH = './musics'

def find_music(noteString):
	musicPath = os.listdir(MUSICS_PATH)
	return musicPath

print(find_music('n'))