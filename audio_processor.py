from config import (
	SAMPLE_RATE,
)

from frequency_extractor import freq_from_autocorr

def process_audio_forever(frameProvider):
	while(True):
		frame = frameProvider.getFrame()
		frameFrequency = freq_from_autocorr(np.fromstring(frame, np.int16), SAMPLE_RATE)

		noteString = find_note_string(find_note_id(frameFrequency)) 

		#todo play audio