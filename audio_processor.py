from notes_tools import find_note_id, find_note_string, volume_too_low, convert_to_32bit_array
from frequency_extractor import freq_from_autocorr
from audio_player import play_music
import pyaudio
import numpy as np
import time

def process_audio_forever(audioRecorder):
	while(True):
		frame = audioRecorder.getFrame()

		if(audioRecorder.input_format == pyaudio.paInt16):
			amplitudeArray = np.fromstring(frame, np.int16)
		else:
			frame = convert_to_32bit_array(frame, audioRecorder.input_format)
			amplitudeArray = np.fromstring(frame, np.int32)

		if not volume_too_low(amplitudeArray, audioRecorder.min_volume):
			frameFrequency = freq_from_autocorr(amplitudeArray, audioRecorder.input_sample_rate)
			
			if(frameFrequency):
				noteString = find_note_string(find_note_id(frameFrequency)) 
				print("Note:", noteString)

				play_music(noteString)