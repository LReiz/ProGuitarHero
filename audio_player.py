import os
import pyaudio
import wave

from config import (
	OUTPUT_SAMPLE_RATE,
	OUTPUT_CHANNELS,
	OUTPUT_SAMPLE_PER_FRAME,
	OUTPUT_FORMAT
)

MUSICS_LIST_PATH = './musics'

def find_music_path(noteString):
	dirFiles = os.listdir(MUSICS_LIST_PATH)
	musicFile = ''
	for index in range(len(dirFiles)):
		if noteString == dirFiles[index].split()[0]:
			musicFile = dirFiles[index]
			break

	if musicFile == '':
		return False

	return (MUSICS_LIST_PATH + '/' + musicFile)

def play_music(noteString):
	musicPath = find_music_path(noteString)

	if not musicPath:
		return
	else:
		musicFile = wave.open(musicPath, 'rb')
		pyaudioInstance = pyaudio.PyAudio()
		streamMediaPlayer = pyaudioInstance.open(rate=OUTPUT_SAMPLE_RATE,
												channels=OUTPUT_CHANNELS,
												format=OUTPUT_FORMAT,
												output=True)

		data = musicFile.readframes(OUTPUT_SAMPLE_PER_FRAME)
		streamMediaPlayer.write(data)

		while (len(data) > 0):
			data = musicFile.readframes(OUTPUT_SAMPLE_PER_FRAME)
			streamMediaPlayer.write(data)
