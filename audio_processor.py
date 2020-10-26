from config import (
	INPUT_SAMPLE_RATE,
)

from notes_tools import find_note_id, find_note_string, volume_too_low
from frequency_extractor import freq_from_autocorr
from audio_player import play_music
import numpy as np

def process_audio_forever(audioRecorder):
	while(True):
		frame = audioRecorder.getFrame()

		amplitudeArray = np.fromstring(frame, np.int16)

		if not volume_too_low(amplitudeArray):
			frameFrequency = freq_from_autocorr(amplitudeArray, INPUT_SAMPLE_RATE)
			print(max(amplitudeArray))
			noteString = find_note_string(find_note_id(frameFrequency)) 

			play_music(noteString)